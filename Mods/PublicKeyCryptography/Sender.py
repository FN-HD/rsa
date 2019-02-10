class Sender:
    def __init__(self, cryptography, key):
        self.cryptography = cryptography
        self.publicKey = key

    def crypt(self, m):
        return self.cryptography.crypt(self.publicKey, m)

    def __str__(self):
        return 'Sender:'+\
               '\n    Cryptography='+str(self.cryptography)+\
               '\n    public key='+str(self.publicKey)
