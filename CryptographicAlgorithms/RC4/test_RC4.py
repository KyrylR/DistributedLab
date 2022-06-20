import unittest
from rc4 import *


class RC4TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plain_text = "Entered plain text"
        cls.init_key = initialize([ord(char) for char in "key_input"])

    def test_encryption_decryption(self):
        print(f'Your plain text is: {self.plain_text}')
        cipher_test, encrypting_key_test = encrypt_rc4(self.init_key, self.plain_text)
        print(f'Your RC4 text is: {repr(cipher_test)}')
        decrypted_text_test = decryption_rc4(cipher_test, encrypting_key_test)
        print(f'Decryption: {decrypted_text_test}\n')
        self.assertEqual(self.plain_text, decrypted_text_test)  # add assertion here


if __name__ == '__main__':
    unittest.main()
