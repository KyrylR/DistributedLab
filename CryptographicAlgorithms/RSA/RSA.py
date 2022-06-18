import random

"""
RSA (Rivest–Shamir–Adleman) is a public-key crypto system that is widely used for secure data transmission. It is 
also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, 
who publicly described the algorithm in 1977. An equivalent system was developed secretly in 1973 at GCHQ (the 
British signals intelligence agency) by the English mathematician Clifford Cocks. That system was declassified in 
1997. 
"""


def egcd(b: int, n: int) -> (int, int, int):
    """
    In arithmetic and computer programming, the extended Euclidean algorithm is an extension to the Euclidean
    algorithm, and computes, in addition to the greatest common divisor (gcd) of integers a and b,
    also the coefficients of Bezout's identity, which are integers x and y such that
    ax + by = gcd(a, b).

    Given two integers ``b`` and ``n``
    returns ``(gcd(b, n), a, m)`` such that ``a*b + n*m == gcd(b, n)``.
    """
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return b, x0, y0


def gcd(p: int, q: int) -> int:
    """
    Euclidian algorithm to find gcd of p qnd q
    :param p: integer
    :param q: integer
    :return: Greatest common divisor od p and q
    """
    while q:
        p, q = q, p % q
    return p


def rabin_miller(n: int, c: int):
    """
    This function is called for all k trials. It returns
    false if n is composite and returns false if n is
    probably prime. c is an
    :param n:
    :param c: odd number such that d*2<sup>r</sup> = n-1 for some r >= 1
    :return:
    """

    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4)

    # Compute a^d % n
    x = pow(a, c, n)

    if x == 1 or x == n - 1:
        return True

    # Keep squaring x while one of the following doesn't happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while c != n - 1:
        x = pow(x, 2, n)
        c *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    # Return composite
    return False


def is_prime(n: int):
    """
    Checking for prime numbers using the Roben-Miller algorithm
    :param n: integer
    :return: True if n prime
    """

    # Check for 0 and 1
    if n < 2:
        return False

    if n in low_primes:
        return True

    for prime in low_primes:
        if n & prime == 0:
            return False

    # find number c such that c * 2 ^ r = n - 1
    c = n - 1  # c even bc n not divisible by 2
    while c % 2 == 0:
        c //= 2  # make c odd

    for i in range(128):
        if not rabin_miller(n, c):
            return False

    return True


def generate_large_prime(size: int) -> int:
    """
    :param size: number of bits in randomly generated prime number
    :return: random large number.
    """
    while True:
        num = random.randrange(2 ** (size - 1), 2 ** size - 1)
        if is_prime(num):
            return num


# low primes to save time
low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
              613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
              751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
              887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def is_co_prime(first: int, second: int) -> bool:
    """
    :param first: first
    :param second: integers
    :return: True if gcd(p, q) is 1
    """
    return gcd(first, second) == 1


def modular_inverse(a: int, b: int) -> int:
    """
    In mathematics, particularly in the area of arithmetic, a modular multiplicative inverse of
    an integer `a` is an integer x such that the product ax is congruent to 1 with respect to the modulus m.
    In the standard notation of modular arithmetic this congruence is written as
    ax ≡ 1 (mod m)
    :param a:
    :param b:
    :return: multiplicative inverse of an integer a
    """
    _, x, _ = egcd(a, b)

    if x < 0:
        x += b

    return x


def generate_keys(k_size: int = 1024) -> (int, int, int):
    """
    Generate public and private keys
    :param k_size: size of keys (number of bits)
    :return: public key, private key, rsa modulas
    """
    # get prime numbers, p & q
    p, q = generate_large_prime(k_size), generate_large_prime(k_size)

    # RSA modulas
    n = p * q

    phi_n = (p - 1) * (q - 1)

    # Choose public key (pbk), where pbk is co-prime with phi_n & 1 < pbk <= phi_n
    while True:
        pbk = random.randrange(2 ** (k_size - 1), 2 ** k_size - 1)
        if is_co_prime(pbk, phi_n):
            break

    # Choose private key (pk), where pk is mod inv of pbk with respect to phi_n ->
    # pbk * pk (mod phi_n) = 1
    pk = modular_inverse(pbk, phi_n)
    return pbk, pk, n


def encrypt(public_key: int, rsa_mod: int, msg: bytes):
    """
    Cipher message byte by byte (c):
    cipher_c = c ^ public_key (mod rsa_mod)
    :param public_key: public key
    :param rsa_mod: RSA modulas
    :param msg: sequence of bytes
    :return: cipher text
    """
    cipher = ""
    for c in bytearray(msg):
        cipher += str(pow(c, public_key, rsa_mod)) + " "

    return cipher


def decrypt(private_key: int, rsa_mod: int, cipher):
    """
    Decrypt message part by part:
    part = cipher_part ^ private_key (mod rsa_mod)
    :param private_key: private key
    :param rsa_mod: RSA modulas
    :param cipher: cipher text
    :return: decrypted cipher
    """
    decrypt_msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            decrypt_msg += chr(pow(c, private_key, rsa_mod))

    return decrypt_msg


if __name__ == '__main__':
    plain_text = "Hello!"
    key_size = 16
    pub_key, pr_key, modulas_rsa = generate_keys(key_size)

    enc = encrypt(pub_key, modulas_rsa, plain_text.encode())
    dec = decrypt(pr_key, modulas_rsa, enc)

    print(f"Message: {plain_text}")
    print(f"Encrypt: {enc}\nDecrypt: {dec}")
