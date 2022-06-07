import unittest
from HashAlgorithms.hash_lib.SHA1.SHA1 import SHA1


class MyTestCase(unittest.TestCase):
    def test_on_keccak_strings(self):
        actual = "Keccak"
        expected = "34a663a04dabe538f7e6b01cb2e4727d55d1364b"
        self.assertEqual(SHA1().encrypt(actual), expected)

    def test_on_long_strings(self):
        actual = "SHA1 and other hash functions online generator"
        expected = "7e16b5527c77ea58bac36dddda6f5b444f32e81b"
        self.assertEqual(SHA1().encrypt(actual), expected)

    def test_on_number_strings(self):
        actual = "123123123"
        expected = "88ea39439e74fa27c09a4fc0bc8ebe6d00978392"
        self.assertEqual(SHA1().encrypt(actual), expected)


if __name__ == '__main__':
    unittest.main()
