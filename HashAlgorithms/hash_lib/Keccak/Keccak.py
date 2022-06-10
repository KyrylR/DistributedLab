import numpy as np
from numpy import bitwise_xor as xor
import io


class Utils:
    @staticmethod
    def array_copy(src, src_pos, dest, dest_pos, length):
        for i in range(length):
            dest[i + dest_pos] = src[i + src_pos]

    @staticmethod
    def little_endian_to_64(data):
        result = 0
        for i in range(0, 8):
            result += int(data[i]) << (8 * i)

        return result

    @staticmethod
    def val_64_to_little_endian(data):
        result = np.zeros(8, dtype=np.ulonglong)
        for i in range(0, 8):
            result[i] = (int(data) >> (8 * i)) % 256

        return result


BIT_64 = 0xffffffffffffffff


class Keccak:
    __slots__ = ['rate', 'd', 'output_len']

    def __init__(self):
        self.rate = 1088
        self.d = np.array(0x01, dtype=np.uint64)
        self.output_len = 256

    @staticmethod
    def _left_circular_shift(n, d):
        """
        Function to left rotate n by d bits
        :param n: the value to be rotated
        :param d: number of bits to shift
        :return: left rotate n by d bits
        """
        d = d % 64
        return ((int(n) << d) | (int(n) >> (64 - d))) & BIT_64

    def encrypt(self, message):
        states = np.zeros(200, dtype=np.uint64)
        bytes_message = np.array([b for b in bytearray(message.encode())], dtype=np.uint64)
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
                states[i] = xor(states[i], bytes_message[i + input_offset])

            input_offset = input_offset + block_size
            if block_size == rate_in_bytes:
                self.keccak_fill(states)
                block_size = 0

        states[block_size] = xor(states[block_size], self.d)
        if (np.bitwise_and(self.d, np.array(0x80, dtype=np.uint64))) != 0 and block_size == (rate_in_bytes - 1):
            self.keccak_fill(states)

        states[rate_in_bytes - 1] = xor(states[rate_in_bytes - 1], np.array(0x80, dtype=np.uint64))
        self.keccak_fill(states)

        byte_results = bytearray()
        temp_output_length = self.output_len // 8
        while temp_output_length > 0:
            block_size = min(temp_output_length, rate_in_bytes)
            for i in range(0, block_size):
                temp = states[i]
                byte_results.append(temp)

            temp_output_length -= block_size
            if temp_output_length > 0:
                self.keccak_fill(states)

        return byte_results

    def keccak_fill(self, states):
        l_state = np.zeros((5, 5), dtype=np.uint64)

        for i in range(0, 5):
            for j in range(0, 5):
                data = np.zeros(8, dtype=np.uint64)
                Utils.array_copy(states, 8 * (i + 5 * j), data, 0, 8)
                l_state[i][j] = Utils.little_endian_to_64(data)

        self.round_b(l_state)
        states.fill(0)
        for i in range(0, 5):
            for j in range(0, 5):
                data = Utils.val_64_to_little_endian(l_state[i][j])
                Utils.array_copy(data, 0, states, 8 * (i + 5 * j), 8)

    def round_b(self, state):
        lfsr_state = 1
        for round_cipher in range(0, 24):
            c_arr = np.zeros(5, dtype=np.uint64)
            d_arr = np.zeros(5, dtype=np.uint64)

            for i in range(0, 5):
                c_arr[i] = xor(xor(xor(xor(state[i][0], state[i][1]), state[i][2]), state[i][3]), state[i][4])

            for i in range(0, 5):
                arg2 = np.array(self._left_circular_shift(c_arr[(i + 1) % 5], 1), dtype=np.uint64)
                arg1 = np.array(c_arr[(i + 4) % 5], dtype=np.uint64)
                d_arr[i] = xor(arg1, arg2)

            for i in range(0, 5):
                for j in range(0, 5):
                    state[i][j] = xor(state[i][j], d_arr[i])

            x, y = 1, 0
            current = state[x][y]
            for i in range(0, 24):
                temp_x = x
                x = y
                y = (2 * temp_x + 3 * y) % 5

                shift_value = current
                current = state[x][y]

                state[x][y] = self._left_circular_shift(shift_value, (i + 1) * (i + 2) // 2)

            for j in range(0, 5):
                temp = np.zeros(5, dtype=np.uint64)
                for i in range(0, 5):
                    temp[i] = state[i][j]

                for i in range(0, 5):
                    invert_value = xor(temp[(i + 1) % 5], BIT_64)
                    state[i][j] = xor(temp[i], np.bitwise_and(invert_value, temp[(i + 2) % 5]))

            for i in range(0, 7):
                lfsr_state = (xor((lfsr_state << 1), ((lfsr_state >> 7) * 0x71))) % 256
                bit_position = (1 << i) - 1
                if (lfsr_state & 2) != 0:
                    state[0][0] = xor(state[0][0], np.array((1 << bit_position), dtype=np.uint64))


if __name__ == "__main__":
    print(f"Hash: {Keccak().encrypt('b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bfb72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff2db60086f59a5dd7dd62c51bf07630f2eaea92b72e67722ec75312c351d0deff207630f2eaea92b72e67722ec75312c351d0deff2').hex()}", end='\n')
