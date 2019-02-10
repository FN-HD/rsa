import math
import random


class Calculation:
    @staticmethod
    def chrlist(i):
        return ''.join([chr(code) for code in i])

    # 拡張ユーグリッドの互除法
    @staticmethod
    def extgcd(x, y):
        if y == 0:
            u = 1
            v = 0
        else:
            (u0, v0) = Calculation.extgcd(y, x % y)
            u = v0
            v = u0 - (x//y)*v0
        return [u, v]

    @staticmethod
    def get_int(a, b=0, c=4):
        primes = [i for i in range(10 ** b, 10 ** c) if math.gcd(a, i) == 1]
        return primes[int(len(primes) * random.random())]

    @staticmethod
    def get_int_size(n):
        return int(math.log10(n))

    @staticmethod
    def lcm(p, q):
        return int(p * q / math.gcd(p, q))

    @staticmethod
    def ordstr(c):
        return [ord(i) for i in c]

    # (m**e)%n
    @staticmethod
    def pow_in_residue_n(m, e, n):
        m1 = 1

        for i in range(e):
            m1 = (m1 * m) % n

        return m1
