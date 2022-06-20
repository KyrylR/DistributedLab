import unittest
from RSA import *


class RSATestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plain_text = "Hello!"
        cls.pub_key, cls.pr_key, cls.modulas_rsa = generate_keys(16)

    def test_encryption_decryption(self):
        print(f"Public key: {self.pub_key}\nPrivate key: {self.pr_key}\nRSA Modulas: {self.modulas_rsa}")
        enc_msg = encrypt(self.pub_key, self.modulas_rsa, self.plain_text.encode())
        dec_msg = decrypt(self.pr_key, self.modulas_rsa, enc_msg)
        print(f"Message: {self.plain_text}")
        print(f"Encrypt: {enc_msg}\nDecrypt: {dec_msg}")
        self.assertEqual(self.plain_text, dec_msg)  # add assertion here


if __name__ == '__main__':
    unittest.main()
