class Receiver:
    def __init__(self, cryptography, o):
        self.cryptography = cryptography
        (self.publicKey, self.privateKey) = cryptography.get_key(o)

    def get_public_key(self):
        return self.publicKey

    def get_private_key(self):
        return self.privateKey

    def decrypt(self, m):
        return self.cryptography.decrypt(self.privateKey, m)

    def __str__(self):
        return 'Receiver:'+\
               '\n    Cryptography='+str(self.cryptography)+\
               '\n    public key='+str(self.publicKey)+\
               '\n    private key='+ str(self.privateKey)
