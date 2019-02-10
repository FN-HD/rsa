from Mods.Math.Calculation import Calculation
from Mods.PublicKeyCryptography.Key import Key
from Mods.PublicKeyCryptography.Cryptography import Cryptography
import math


class RSA(Cryptography):
    # this calculation is f(m) = m**e % n. (e, n) = key
    @staticmethod
    def calculate(key, m):
        (e, n) = key.get_key()
        return Calculation.pow_in_residue_n(m, e, n)

    @staticmethod
    def crypt(key, m):
        if isinstance(m, int):
            return RSA.calculate(key, m)
        elif isinstance(m, str):
            return [RSA.crypt(key, s) for s in Calculation.ordstr(m)]
        else:
            raise TypeError('you should input int or str')

    @staticmethod
    def decrypt(key, c):
        if isinstance(c, int):
            return RSA.calculate(key, c)
        elif isinstance(c, list):
            return Calculation.chrlist([RSA.decrypt(key, s) for s in c])
        else:
            raise TypeError('you should input int or list')

    @staticmethod
    def get_key(data):
        (p, q) = data
        n = p * q
        lam = Calculation.lcm(p-1, q-1)
        # we create public key
        e = RSA.get_public_key_exp(lam)
        # we create private key
        d = RSA.get_private_key_exp(e, lam)

        # (public key, private key)
        return [Key((e, n)), Key((d, n))]

    @staticmethod
    def get_public_key_exp(lam):
        size = Calculation.get_int_size(lam)
        return Calculation.get_int(lam,  size, size+1)

    @staticmethod
    def get_private_key_exp(e, lam):
        d = Calculation.extgcd(e, lam)[0]

        if d < 0:
            d = d + lam

        return d
