from Mods.Math.Calculation import Calulation
from Mods.PublicKeyCryptography.Key import PublicKey
from Mods.PublicKeyCryptography.Key import PrivateKey
from Mods.PublicKeyCryptography.Cryptography import Cryptography
import math


class RSA(Cryptography):
    @staticmethod
    def crypt(key, m):
        if isinstance(m, int):
            m1 = 1
            (e, n) = key.get_key()

            for i in range(e):
                m1 = (m1*m) % n

            return m1
        elif isinstance(m, str):
            return [RSA.crypt(key, s) for s in Calulation.ordstr(m)]

    @staticmethod
    def decrypt(key, c):
        if isinstance(c, int):
            c1 = 1
            (d, n) = key.get_key()

            for i in range(d):
                c1 = (c1*c) % n

            return c1
        elif isinstance(c, list):
            return Calulation.chrlist([RSA.decrypt(key, s) for s in c])

    @staticmethod
    def get_key(data):
        (p, q) = data
        n = p * q
        lam = RSA.get_lambda(p-1, q-1)
        e = RSA.get_public_key_exp(lam)
        d = RSA.get_private_key_exp(e, lam)

        return (PublicKey((e, n)), PrivateKey((d, n)))

    @staticmethod
    def get_lambda(p, q):
        return int(p*q / math.gcd(p, q))

    @staticmethod
    def get_public_key_exp(lam):
        size = int (math.log10(lam))
        return Calulation.get_int(lam,  size, size+1)

    @staticmethod
    def get_private_key_exp(e, lam):
        d = Calulation.extgcd(e, lam)[0]

        if d < 0:
            d = d + lam

        return d