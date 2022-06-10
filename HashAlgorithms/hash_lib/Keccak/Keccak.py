import numpy as np
import io
import struct


# Future utils
def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]


BIT_64 = 0xffffffffffffffff


class Keccak:
    __slots__ = ['rate', 'd', 'output_len']

    def __init__(self):
        self.rate = 1088
        self.d = 0x01
        self.output_len = 256

    @staticmethod
    def _left_circular_shift(n, d):
        """
        Function to left rotate n by d bits
        :param n: the value to be rotated
        :param d: number of bits to shift
        :return: left rotate n by d bits
        """
        return ((n << d) | (n >> (64 - d))) & BIT_64

    def encrypt(self, message):
        states = np.array(200)
        bytes_message = np.array(message.encode())
        bytes_length = len(message)

        if self.rate % 8 != 0:
            print("Error!")
            return

        rate_in_bytes = self.rate // 8
        block_size = 0
        input_offset = 0

        while input_offset < bytes_length:
            block_size = min(bytes_length - input_offset, rate_in_bytes)
            for i in range(0, block_size):
                states[i] = states[i] ^ bytes_message[i + input_offset]

            input_offset = input_offset + block_size
            if block_size == rate_in_bytes:
                self.keccak_fill(states)
                block_size = 0

    def keccak_fill(self, states):
        l_state = np.zeros((5, 5))

        for i in range(0, 5):
            for j in range(0, 5):
                data = np.zeros(8)
                array_copy(states, 8 * (i + 5 * j), data, 0, 8)
                l_state[i][j] = struct.pack(b'>Q', data)

    def round_b(self, state):
        lfsr_state = 1
        for round in range(0, 24):
            C = np.array(5)
            D = np.array(5)

            for i in range(0, 5):
                C[i] = state[i][0] ^ state[i][1] ^ state[i][2] ^ state[i][3] ^ state[i][4]

            for i in range(0, 5):
                D[i] = C[(i + 4) % 5] ^ self._left_circular_shift(C[(i + 1) % 5], 1)

            for i in range(0, 5):
                for j in range(0, 5):
                    state[i][j] = state[i][j] ^ D[i]

            x, y = 1, 0
            current = state[x][y]
            for i in range(0, 24):
                temp_x = x
                x = y
                y = (2 * temp_x + 3 * y) % 5

                shift_value = current
                current = state[x][y]

                state[x][y] = self._left_circular_shift(shift_value, (i + 1) * (i + 2) / 2)

            for j in range(0, 5):
                temp = np.array(5)
                for i in range(0, 5):
                    temp[i] = state[i][j]

                for i in range(0, 5):
                    invert_value = temp[(i + 1) % 5] ^ BIT_64
                    state[i][j] = temp[i] ^ (invert_value + temp[(i + 2) % 5])

            for i in range(0, 7):
                lfsr_state = ((lfsr_state << 1) ^ ((lfsr_state >> 7) * 0x71)) % 256
                bit_position = (1 << i) - 1
                if (lfsr_state & 2) != 0:
                    state[0][0] = state[0][0] ^ (1 << bit_position)

