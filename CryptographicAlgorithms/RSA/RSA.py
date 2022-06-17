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
        x += 1

    return x


def generate_keys():
    p, q = 11, 13
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 13
    d = modular_inverse(e, phi_n)
    return e, d, n


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
    pub_key, pr_key, module_n = generate_keys()

    enc = encrypt(pub_key, module_n, plain_text)
    dec = decrypt(pr_key, module_n, enc)

    print(f"Message: {plain_text}")
    print(f"Encrypt: {enc}\nDecrypt: {dec}")
