class Receiver:
    def __init__(self, cryptography, o):
        self.cryptography = cryptography
        (self.publicKey, self.privateKey) = cryptography.get_key(o)

    def get_key(self):
        return self.publicKey

    def decrypt(self, m):
        return self.cryptography.decrypt(self.privateKey, m)
