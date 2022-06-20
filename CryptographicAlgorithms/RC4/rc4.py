"""
------------------------------------------------Theory------------------------------------------------------------------
RC4 generates a pseudorandom stream of bits (a key-stream). As with any stream cipher,
these can be used for encryption by combining it with the plaintext using bit-wise exclusive-or;
decryption is performed the same way (since exclusive-or with given data is an involution).
This is similar to the one-time pad except that generated pseudorandom bits, rather than a prepared stream, are used.

To generate the key-stream, the cipher makes use of a secret internal state which consists of two parts:
    A permutation of all 256 possible bytes (denoted "S" below).
    Two 8-bit index-pointers (denoted "i" and "j").

The permutation is initialized with a variable length key, typically between 40 and 2048 bits,
using the key-scheduling algorithm (KSA). Once this has been completed, the stream of bits is
generated using the pseudo-random generation algorithm (PRGA).
---------------------------------------------------End------------------------------------------------------------------
:author: ryabov.kiril@knu.ua
"""


def initialize(key_str: list):
    """
    Produce a 256-entry list based on `key` (a sequence of numbers)
    as the first step in RC4.
    Note: indices in key greater than 255 will be ignored.
    """
    key = list(range(256))
    j = 0
    for i in range(256):
        j = (j + key[i] + key_str[i % len(key_str)]) % 256
        key[i], key[j] = key[j], key[i]
    return key


def random_bytes_generator(k):
    """
    Yield a pseudo-random stream of bytes based on 256-byte array `k`.
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        k[i], k[j] = k[j], k[i]
        yield k[(k[i] + k[j]) % 256]


def run_rc4(k, text):
    cipher_chars = []
    key = []
    gen = random_bytes_generator(k)
    for char in text:
        byte = ord(char)
        next_gen = next(gen)
        key.append(next_gen)
        cipher_byte = byte ^ next_gen
        cipher_chars.append(chr(cipher_byte))
    return ''.join(cipher_chars), key


def decryption_rc4(text, key):
    cipher_chars = []
    for itr, char in enumerate(text):
        byte = ord(char)
        next_key = key[itr]
        cipher_byte = byte ^ next_key
        cipher_chars.append(chr(cipher_byte))
    return ''.join(cipher_chars)


def encrypt_rc4(key_chars: list, plain: str):
    """
    Present a command-line interface to the cipher.
    """
    # Acquire initial cipher values.
    return run_rc4(list(key_chars), plain)


if __name__ == '__main__':
    key_input = input('Enter an encryption key: ' + '\n')
    key_char_list = [ord(char) for char in key_input]
    plain_text = input('Enter plain or cipher text(or 0 to quit): ')
    init_key = initialize(key_char_list)
    cipher, encrypting_key = encrypt_rc4(init_key, plain_text)
    print(f'Your RC4 text is: {repr(cipher)}\n')
    decrypted_text = decryption_rc4(cipher, encrypting_key)
    print(f'Decryption: {repr(decrypted_text)}\n')
