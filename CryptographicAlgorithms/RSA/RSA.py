import random

"""

"""


def egcd(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def modular_inverse(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


def rabin_miller(n, c):
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


def generate_large_prime(size) -> int:
    """
    :param size: number of bits in randomly generated prime number
    :return: random large number.
    """
    while True:
        num = random.randrange(2 ** (size - 1), 2 ** size - 1)
        if is_prime(num):
            return num


def gcd(p, q):
    """
    Euclidian algorithm to find gcd of p qnd q
    :param p, q: integers
    :return: Greatest common divisor od p and q
    """
    while q:
        p, q = q, p % q
    return p


# low primes to save time
low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
              613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
              751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
              887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def is_prime(n):
    """
    Fall back to rabin miller if uncertain.
    :param n: integer
    :return: True if n prime
    """

    # 0, 1 -re numbers not prime
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


def is_co_prime(p: int, q: int) -> bool:
    """
    :param p, q: integers
    :return: True if gcd(p, q) is 1
    """
    return gcd(p, q) == 1


def generate_keys(k_size=1024):
    # get prime numbers, p & q
    p, q = generate_large_prime(k_size), generate_large_prime(k_size)

    # RSA modulas
    n = p * q

    phi_n = (p - 1) * (q - 1)

    # Choose public key (pbk), where pbk is co-prime with phi_n & 1 < pbk <= phi_n
    while True:
        pbk = random.randrange(2 ** (k_size - 1), 2 ** key_size - 1)
        if is_co_prime(pbk, phi_n):
            break

    # Choose private key (pk), where pk is mod inv of pbk with respect to phi_n ->
    # pbk * pk (mod phi_n) = 1
    pk = modular_inverse(pbk, phi_n)
    return pbk, pk, n


def encrypt(public_key, n, msg):
    cipher = ""
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, public_key, n)) + " "

    return cipher


def decrypt(private_key, n, cipher):
    decrypt_msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            decrypt_msg += chr(pow(c, private_key, n))

    return decrypt_msg


if __name__ == '__main__':
    plain_text = "Hello!"
    key_size = 32
    pub_key, pr_key, module_n = generate_keys(key_size)

    enc = encrypt(pub_key, module_n, plain_text)
    dec = decrypt(pr_key, module_n, enc)

    print(f"Message: {plain_text}")
    print(f"Encrypt: {enc}\nDecrypt: {dec}")
