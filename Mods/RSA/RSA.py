from Mods.Math.Calculation import Calculation
from Mods.Cryptography.Cryptography import Key
from Mods.Cryptography.Cryptography import Cryptography


class RSA(Cryptography):
    # this calculation is f(m) = m**e % n. (e, n) = key
    @staticmethod
    def calculate(key, m):
        (e, n) = key.get_key()
        return Calculation.pow_in_residue_n(m, e, n)

    @staticmethod
    def encrypt(key, m):
        if isinstance(m, int):
            return RSA.calculate(key, m)
        elif isinstance(m, str):
            return [RSA.encrypt(key, s) for s in Cryptography.ordstr(m)]
        else:
            raise TypeError('you should input int or str')

    @staticmethod
    def decrypt(key, c):
        if isinstance(c, int):
            return RSA.calculate(key, c)
        elif isinstance(c, list):
            return Cryptography.chrlist([RSA.decrypt(key, s) for s in c])
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
        digit = Calculation.get_int_digit(lam)
        return Calculation.get_random_prime_int(lam,  10*digit)

    @staticmethod
    def get_private_key_exp(e, lam):
        d = Calculation.extgcd(e, lam)[0]

        if d < 0:
            d = d + lam

        return d
