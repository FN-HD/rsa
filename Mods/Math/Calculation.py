import math
import random


class Calulation:
    @staticmethod
    def get_int(a, b=0, c=4):
        l = [i for i in range(10 ** b, 10 ** c) if math.gcd(a, i) == 1]
        return l[int(len(l) * random.random())]

    #extended euclidean
    @staticmethod
    def extgcd(x, y):
        if y == 0:
            u = 1
            v = 0
        else:
            (u0, v0) = Calulation.extgcd(y, x % y)
            u = v0
            v = u0 - (x//y)*v0
        return (u, v)

    @staticmethod
    def ordstr(c):
        return [ord(i) for i in c]

    @staticmethod
    def chrlist(i):
        return ''.join([chr(code) for code in i])
