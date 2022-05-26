import unittest
from little_big_endian_hex_converter import *


class ConvertorTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        test_data = utils.read_test_from_file()
        cls.vector_list = test_data[0]
        cls.bytes_number_list = test_data[1]
        cls.little_endian_list = test_data[2]
        cls.big_endian_list = test_data[3]

    @classmethod
    def pretty_print(cls, expected, actual):
        print(f"Expected value:\t{expected}")
        print(f"Actual value:\t{actual}\n")

    def test_count_bytes(self):
        for value, result in zip(self.vector_list, self.bytes_number_list):
            actual_value = count_bytes(value)
            expected_value = int(result)
            self.pretty_print(expected_value, actual_value)
            self.assertEqual(actual_value, expected_value)

    def test_hex2little_endian(self):
        for value, result in zip(self.vector_list, self.little_endian_list):
            actual_value = str(hex2little_endian(value))
            expected_value = result
            self.pretty_print(expected_value, actual_value)
            self.assertEqual(actual_value, expected_value)

    def test_hex2big_endian(self):
        for value, result in zip(self.vector_list, self.big_endian_list):
            actual_value = str(hex2big_endian(value))
            expected_value = result
            self.pretty_print(expected_value, actual_value)
            self.assertEqual(actual_value, expected_value)

    def test_little_endian2hex(self):
        for n_bytes, value, result in zip(self.bytes_number_list, self.little_endian_list, self.vector_list):
            actual_value = little_endian2hex(int(value), bytes_number=int(n_bytes))
            expected_value = result
            self.pretty_print(expected_value, actual_value)
            self.assertEqual(actual_value, expected_value)

    def test_big_endian2hex(self):
        for value, result in zip(self.big_endian_list, self.vector_list):
            actual_value = big_endian2hex(int(value))
            expected_value = result
            self.pretty_print(expected_value, actual_value)
            self.assertEqual(actual_value, expected_value)


if __name__ == '__main__':
    unittest.main()
