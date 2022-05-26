from enum import Enum


class Type(Enum):
    VALUE = 'value'
    BYTES_NUMBER = 'n_bytes'
    LITTLE_ENDIAN = 'little'
    BIG_ENDIAN = 'big'


def read_data_from_file(filepath: str):
    """
    Getting data from a file

    :param filepath: path to data file
    :return: list of vectors
    """
    try:
        with open(filepath, mode='r+') as data_file:
            vector_list = []
            for line in data_file:
                if not line.startswith("#"):
                    vector_list.append(line.replace("\n", ""))

            return vector_list
    except FileNotFoundError as err:
        print('File do not exist')
        raise err
    except IOError as err:
        print('IO error')
        raise err


def read_test_from_file():
    """
    Getting test values from a file

    :param filepath: path to data file
    :return: vector list, bytes number list, little endian list, big endian list as tuple
    """
    try:
        with open('data/test_data.txt', mode='r+') as data_file:
            vector_list = []
            bytes_number_list = []
            little_endian_list = []
            big_endian_list = []
            for line in data_file:
                if not line.startswith("#") and len(line.replace('\n', '')) != 0:
                    data_list = list(map(str, line.split(': ')))
                    if data_list[0] == Type.VALUE.value:
                        vector_list.append(data_list[1].replace("\n", "").lower())
                        continue
                    if data_list[0] == Type.BYTES_NUMBER.value:
                        bytes_number_list.append(data_list[1].replace("\n", "").lower())
                        continue
                    if data_list[0] == Type.LITTLE_ENDIAN.value:
                        little_endian_list.append(data_list[1].replace("\n", "").lower())
                        continue
                    if data_list[0] == Type.BIG_ENDIAN.value:
                        big_endian_list.append(data_list[1].replace("\n", "").lower())

            return vector_list, bytes_number_list, little_endian_list, big_endian_list
    except FileNotFoundError as err:
        print('File do not exist')
        raise err
    except IOError as err:
        print('IO error')
        raise err
