import math
import random


class Calculation:
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

    # we can get the number prime to a.
    @staticmethod
    def get_random_prime_int(a, b=0, c=0):

        if c > a or b > c:
            c = a

        primes = [i for i in range(b, c) if math.gcd(a, i) == 1]
        return primes[int(len(primes) * random.random())]

    # we can get integer digit.
    @staticmethod
    def get_int_digit(n):
        return int(math.log10(n))

    # we can get least common multiplier.
    @staticmethod
    def lcm(p, q):
        return int(p * q / math.gcd(p, q))

    # (m**e)%n
    @staticmethod
    def pow_in_residue_n(m, e, n):
        m1 = 1

        for i in range(e):
            m1 = (m1 * m) % n

        return m1
