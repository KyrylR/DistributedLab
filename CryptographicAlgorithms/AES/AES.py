# Fixed table for encryption
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

# Fixed table for decryption
inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)


# Check https://www.youtube.com/watch?v=CADQLQyeLgU :)
def x_time(a: int) -> int:
    """
    Multiplication by x
    Examples:
    1. 57’ • ‘02’ = xtime(57) = ‘BF’
    2. ‘57’ • ‘04’ = xtime(BF) = ‘64’
    3. ‘57’ • ‘08’ = xtime(64) = ‘C8’
    4. ‘57’ • ‘10’ = x_time(C8) = ‘8B’
    5. ‘57’ • ‘13’ = ‘57’ • (‘01’ ⊕ ‘02’ ⊕ ‘10’ ) = ‘57’ ⊕ ‘BF’ ⊕ ‘8B’ = ‘63’
    """
    return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


# The round constant word array
Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)


def divide_into_blocks(text: int) -> list:
    """
    The function divides the input text into blocks of 128 bits (16 bytes).
    Each block is represented as a 4x4 matrix
    :param text: plain integer value
    :return: 4x4 matrix
    """
    matrix = []
    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xFF
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[i // 4].append(byte)
    return matrix


def merge_into_string(matrix: list) -> int:
    """
    The function combines a 4x4 input matrix into a single integer row.
    :param matrix: 4x4 matrix
    :return: single integer line
    """
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[i][j] << (120 - 8 * (4 * i + j)))
    return text


class AES:
    """
    The Advanced Encryption Standard (AES), also known by its original name Rijndael.
    AES is based on a design principle known as a substitution–permutation network, and is efficient in both software
    and hardware. Unlike its predecessor DES, AES does not use a Feistel network. AES is a variant of Rijndael, with
    a fixed block size of 128 bits, and a key size of 128, 192, or 256 bits. By contrast, Rijndael per se is specified
    with block and key sizes that may be any multiple of 32 bits, with a minimum of 128 and a maximum of 256 bits.
    :href: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
    """
    __slots__ = ['round_keys', 'plain_state', 'cipher_state']

    def __init__(self, master_key):
        """
        AES initialization.
        :param master_key: The Cipher Key
        """
        self.cipher_state = []
        self.plain_state = []
        self.round_keys = []
        self.get_round_keys(master_key)

    def get_round_keys(self, master_key):
        """
        The function performs key expansion. Since AES assumes a key length of 128 bits (in the simplest case), this
        means that a key sequence equal to the length of the message to be encrypted must be generated for longer data.
        This is what the deployment function is used for
        (a separate 128-bit encryption key is generated for each encrypted block).
        :param master_key: The Cipher Key
        :return: generate a series of Round Keys from the Cipher Key
        """
        self.round_keys = divide_into_blocks(master_key)

        for i in range(4, 4 * 11):
            self.round_keys.append([])
            if i % 4 == 0:
                byte = self.round_keys[i - 4][0] ^ s_box[self.round_keys[i - 1][1]] ^ Rcon[i // 4]
                self.round_keys[i].append(byte)

                for j in range(1, 4):
                    byte = self.round_keys[i - 4][j] ^ s_box[self.round_keys[i - 1][(j + 1) % 4]]
                    self.round_keys[i].append(byte)
            else:
                for j in range(4):
                    byte = self.round_keys[i - 4][j] ^ self.round_keys[i - 1][j]
                    self.round_keys[i].append(byte)

    def encrypt(self, plaintext):
        """
        Series of transformations that converts plaintext to ciphertext using the Cipher Key.
        :param plaintext: Data input to the Cipher.
        :return: encrypted text (ciphertext)
        """
        self.plain_state = divide_into_blocks(plaintext)

        self.__add_round_key(self.plain_state, self.round_keys[:4])

        for i in range(1, 10):
            self.__sub_bytes(self.plain_state)
            self.__shift_rows(self.plain_state)
            self.__mix_columns(self.plain_state)
            self.__add_round_key(self.plain_state, self.round_keys[4 * i: 4 * (i + 1)])

        self.__sub_bytes(self.plain_state)
        self.__shift_rows(self.plain_state)
        self.__add_round_key(self.plain_state, self.round_keys[40:])

        return merge_into_string(self.plain_state)

    def decrypt(self, ciphertext):
        """
        Series of transformations that converts ciphertext to plaintext using the Cipher Key.
        :param ciphertext: Data output from the Cipher.
        :return: decrypted ciphertext
        """
        self.cipher_state = divide_into_blocks(ciphertext)

        self.__add_round_key(self.cipher_state, self.round_keys[40:])
        self.__inv_shift_rows(self.cipher_state)
        self.__inv_sub_bytes(self.cipher_state)

        for i in range(9, 0, -1):
            self.__add_round_key(self.cipher_state, self.round_keys[4 * i: 4 * (i + 1)])
            self.__inv_mix_columns(self.cipher_state)
            self.__inv_shift_rows(self.cipher_state)
            self.__inv_sub_bytes(self.cipher_state)

        self.__add_round_key(self.cipher_state, self.round_keys[:4])

        return merge_into_string(self.cipher_state)

    @staticmethod
    def __add_round_key(s, k):
        """
        Transformation in the Cipher and Inverse Cipher in which a Round
        Key is added to the State using an XOR operation. The length of a
        Round Key equals the size of the State (i.e., for Nb = 4, the Round
        Key length equals 128 bits/16 bytes).
        :param s: State.
        :param k: Cipher Key.
        :return: transformed string.
        """
        for i in range(4):
            for j in range(4):
                s[i][j] ^= k[i][j]

    @staticmethod
    def __sub_bytes(s):
        """
        Transformation in the Cipher that processes the State using a non
        linear byte substitution table (S-box) that operates on each of the
        State bytes independently.
        :param s: State.
        :return: Transformed string.
        """
        for i in range(4):
            for j in range(4):
                s[i][j] = s_box[s[i][j]]

    @staticmethod
    def __inv_sub_bytes(s):
        """
        Transformation in the Inverse Cipher that is the inverse of
        SubBytes().
        :param s: State.
        :return: Transformed string.
        """
        for i in range(4):
            for j in range(4):
                s[i][j] = inv_s_box[s[i][j]]

    @staticmethod
    def __shift_rows(s):
        """
        Transformation in the Cipher that processes the State by cyclically
        shifting the last three rows of the State by different offsets.
        :param s: State.
        :return: Transformed string.
        """
        s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

    @staticmethod
    def __inv_shift_rows(s):
        """
        Transformation in the Inverse Cipher that is the inverse of
        ShiftRows().
        :param s: State.
        :return: Transformed string.
        """
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

    @staticmethod
    def __mix_columns(s):
        """
        Transformation in the Cipher that takes all of the columns of the
        State and mixes their data (independently of one another) to
        produce new columns.
        :param s: State.
        :return: Transformed string.
        """
        for i in range(4):
            t = s[i][0] ^ s[i][1] ^ s[i][2] ^ s[i][3]
            u = s[i][0]
            s[i][0] ^= t ^ x_time(s[i][0] ^ s[i][1])
            s[i][1] ^= t ^ x_time(s[i][1] ^ s[i][2])
            s[i][2] ^= t ^ x_time(s[i][2] ^ s[i][3])
            s[i][3] ^= t ^ x_time(s[i][3] ^ u)

    def __inv_mix_columns(self, s):
        """
        Transformation in the Inverse Cipher that is the inverse of
        MixColumns().
        :param s: State.
        :return: Transformed string.
        """
        for i in range(4):
            u = x_time(x_time(s[i][0] ^ s[i][2]))
            v = x_time(x_time(s[i][1] ^ s[i][3]))
            s[i][0] ^= u
            s[i][1] ^= v
            s[i][2] ^= u
            s[i][3] ^= v

        self.__mix_columns(s)
