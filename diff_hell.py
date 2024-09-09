def is_prime(n):
    if n % 2 == 0:
        return False
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True

from random import randint
import rsa
def main():
    (pubkey, privkey) = rsa.newkeys(512)
    message = 'Finogenov'.encode('utf8')
    print("Текст для шифрования: ", message)

    p = randint(100000000000, 1000000000000)
    while (not is_prime(p)):
        p += 1
    q = randint(1000000000000, 10000000000000)
    while (not is_prime(q)):
        q += 1
    p = 3557
    q = 2579
    crypto = rsa.encrypt(message, pubkey)
    print('Зашифрованый текст', crypto)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    gcd, d, y = euclid_ext(e, phi)
    d %= phi
    if d < 0:
        d += phi
    open_key = (e, n)
    secret_key = (d, n)
    message = rsa.decrypt(crypto, privkey)
    print("Расшифрованный текст: ", message.decode('utf8'))
