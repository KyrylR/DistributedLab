import numpy as np
import io
import struct


# Future utils
def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]


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
        return ((n << d) | (n >> (64 - d))) & 0xffffffffffffffff

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

    def roundB(self, state):
        pass
