import io
import struct

"""
Based on: https://en.wikipedia.org/wiki/SHA-1#SHA-1_pseudocode
"""


class SHA1:
    """
    A class for implementing the SHA1 algorithm.
    """
    __slots__ = ['h']

    def __init__(self):
        # Initialize variables:
        self.h = (
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0,
        )

    @staticmethod
    def _left_circular_shift(n, d):
        """
        Function to left rotate n by d bits
        :param n: the value to be rotated
        :param d: number of bits to shift
        :return: left rotate n by d bits
        """
        return ((n << d) | (n >> (32 - d))) & 0xffffffff

    def _process_chunk(self, chunk, h0, h1, h2, h3, h4):
        """
        Process the message in successive 512-bit chunks
        :param chunk: preprocessed 512-bit chunk
        :return: the final hash value (big-endian) as a 160-bit number
        """
        assert len(chunk) == 64

        # word
        w = [0] * 80

        # Break chunk into sixteen 4-byte big-endian words w[i]
        for i in range(16):
            w[i] = struct.unpack(b'>I', chunk[i * 4:i * 4 + 4])[0]

        # Extend the sixteen 4-byte words into eighty 4-byte words
        for i in range(16, 80):
            w[i] = self._left_circular_shift(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)

        # Initialize hash value for this chunk
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if 0 <= i <= 19:
                # Use alternative 1 for f from FIPS PB 180-1 to avoid bitwise not
                f = d ^ (b & (c ^ d))
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            a, b, c, d, e = ((self._left_circular_shift(a, 5) + f + e + k + w[i]) & 0xffffffff,
                             a, self._left_circular_shift(b, 30), c, d)

        # Add this chunk's hash to result so far
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

        return h0, h1, h2, h3, h4

    def encrypt(self, message: str):
        """
        Produce a hex SHA-1 digest of the input message.

        :param message: plain text
        :return: the final hash value (big-endian) as a hex string
        """
        bytes_message = io.BytesIO(message.encode())
        message_byte_len = 0

        # Read the first block of 512 bits
        block = bytes_message.read(64)

        # Read the rest of the data, 64 bytes at a time
        while len(block) == 64:
            self.h = self._process_chunk(block, *self.h)
            message_byte_len += 64
            block = bytes_message.read(64)

        message_byte_len += len(block)
        # append the bit '1' to the message e.g. by adding 0x80
        # if message length is a multiple of 8 bits.
        block += b'\x80'

        # append 0 <= k < 512 bits '0', so that the resulting message length (in bytes)
        # is congruent to 448 (mod 512) <- bits, so in bytes is -8 = 56 mod 64
        block += b'\x00' * ((56 - (message_byte_len + 1) % 64) % 64)

        # append ml, the original message length in bits, as a 64-bit big-endian integer.
        # Thus, the total length is a multiple of 512 bits.
        block += struct.pack(b'>Q', message_byte_len * 8)

        # Process the final block
        h = self._process_chunk(block[:64], *self.h)
        if len(block) == 64:
            # this string is a concatenation of h0, ..., h4 in hexadecimal format
            # %08x (0xff) equals 4 bytes, so we have 5 * 4 = 20 bytes or 160 bits
            return '%08x%08x%08x%08x%08x' % h

        return '%08x%08x%08x%08x%08x' % self._process_chunk(block[64:], *h)


if __name__ == "__main__":
    print(SHA1().encrypt("Hello world!"))
