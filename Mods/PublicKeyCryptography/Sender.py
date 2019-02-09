class Sender:
    def __init__(self, crptography, key):
        self.cryptography = crptography
        self.key = key

    def crypt(self, m):
        return self.cryptography.crypt(self.key, m)
