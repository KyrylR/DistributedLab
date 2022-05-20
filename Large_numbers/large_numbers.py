from random import getrandbits
from datetime import datetime

"""
A little bit of explanation:
The assignment is completed, based on 
 `PEP 237 – Unifying Long Integers and Integers`
href: https://peps.python.org/pep-0237/

So, to accomplish this task, it will be sufficient 
to use `int` to work on large numbers.
"""


def keys_variety(n: int) -> None:
    """
    Displays the number of keys with of which an n-bit sequence can be specified.
    :param n: Number of bits
    :return: Quantity of keys
    """
    print(f"Variety of keys for {n}: \n {2 ** n:_}\n")


def generate_key(n: int) -> int:
    """
    Generating a random number with a given number of bits
    using the `getrandombits()` function from the Python `random` library.
    :param n: Number of bits
    :return: Random key for given bits
    """
    return getrandbits(n)


def brute_force_hey(real_key, n: int):
    """
    Brute force of values from the range in order to find the key.
    :param real_key: The key that is the target of the attack
    :param n: Number of bits
    :return: time in milliseconds to determine real_key
    """
    start = datetime.now()
    for x in range(0, 2 ** n):
        if real_key == x:
            break
    end = datetime.now()
    return (end - start).microseconds * 10 ** 3


if __name__ == "__main__":
    for i in range(3, 13):
        print("-" * 20)
        # Number of bits
        n = 2 ** i

        # Check the variety of keys with of which an n-bit sequence can be specified.
        keys_variety(n)

        # Generate a pseudo-random key for given n.
        key = generate_key(n)
        print(f"Generated key: {key}\n")

        # It's `if' to see the end of the program in our lives :)
        if i < 6:
            # Brute force of values from the range in order to find the key.
            print(f"It took: {brute_force_hey(key, n)} ms")
            print(f"To determine {key}")
        print("-" * 20 + '\n')
