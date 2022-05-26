import numpy as np
import utils

"""
A little bit of theory:
For calculations, the data is stored in separate fields, each field storing a byte (8 bytes). 
For a single value which exceeds 8 bytes, we can store it as a sequence of bytes. The order in 
which we store the bytes is important (depends on the system in use). Sometimes a storage of 
young bytes in the first memory location is used, and high bytes in the last one. Sometimes in 
the same way. In this case it is important how we convert the hex value to a whole unsigned value.

"""


def count_bytes(vector: str) -> int:
    """
    Byte counting for a given hex value.

    :param vector: String representation of hex value.
    :return: Number of bytes for given vector.
    """
    return int(np.ceil(len(vector) / 2))


def hex2little_endian(vector: str) -> int:
    """
    Conversion of HEX value to Little Endian value.

    :param vector: String representation of hex value.
    :return: integer representation of little endian.
    """
    arr = np.array([vector[i:i + 2] for i in range(0, len(vector), 2)])
    arr[::1].sort(kind='mergesort')
    return int(''.join(''.join(x[0]) for x in zip(arr)), 16)


def hex2big_endian(vector: str) -> int:
    """
    Conversion of HEX value to Big Endian value.

    :param vector: String representation of hex value.
    :return: integer representation of big endian.
    """
    arr = np.array([vector[i:i + 2] for i in range(0, len(vector), 2)])
    arr[::-1].sort(kind='mergesort')
    return int(''.join(''.join(x[0]) for x in zip(arr)), 16)


def little_endian2hex(value: int, bytes_number: int = None) -> str:
    """
    Conversion of Little Endian value to HEX value.

    :param value: integer representation of little endian.
    :param bytes_number: number of bytes from initial value.
    :return: hex string in lowercase.
    """
    hex_value = str(hex(value)).replace('0x', '')
    if bytes_number is not None:
        while len(hex_value) < bytes_number * 2:
            hex_value += '00'
    return hex(int(hex_value, 16)).replace('0x', '').lower()


def big_endian2hex(value: int) -> str:
    """
    Conversion of BIG Endian values into HEX values.

    :param value: integer representation of big endian.
    :return: hex string in lowercase.
    """
    return hex(value).replace('0x', '').lower()


def pretty_print(value: str) -> None:
    """
    Display all function results that can be obtained with a given hex value.

    :param value: String representation of hex value.
    :return: None.
    """
    print("-" * 100)
    print(f"Given value: {value}")

    bytes_n = count_bytes(value)
    print(f"Number of bytes: {bytes_n}")

    little_endian = hex2little_endian(value)
    print(f"Little endian from value: {little_endian}")

    big_endian = hex2big_endian(value)
    print(f"Big endian from value: {big_endian}")

    little_endian_val = little_endian2hex(little_endian, bytes_n)
    print(f"Hex number from Little endian: {little_endian_val}\n"
          f"Number of bytes for Little endian: {count_bytes(str(little_endian_val).replace('0x', ''))}")

    big_endian_val = big_endian2hex(big_endian)
    print(f"Hex number from Big endian: {big_endian_val}\n"
          f"Number of bytes for Big endian: {count_bytes(str(big_endian_val).replace('0x', ''))}")
    print("-" * 100 + '\n')


if __name__ == "__main__":
    vector_list = utils.read_data_from_file("data/data.txt")
    for item in vector_list:
        pretty_print(item)
