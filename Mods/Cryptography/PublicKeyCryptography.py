# receiver in public key cryptography
class Recipient:
    # cryptography is class overridden by Cryptography.
    # o is data to create key.
    def __init__(self, cryptography, o):
        self.cryptography = cryptography
        (self.publicKey, self.privateKey) = cryptography.get_key(o)

    # we can get public key.
    def get_public_key(self):
        return self.publicKey

    # we can get private key
    def get_private_key(self):
        return self.privateKey

    # we can decrypt m by private key
    def decrypt(self, m):
        return self.cryptography.decrypt(self.privateKey, m)

    def __str__(self):
        return 'Recipient:' + \
               '\n    Cryptography='+str(self.cryptography) + \
               '\n    public key='+str(self.publicKey) + \
               '\n    private key='+str(self.privateKey)


# sender in public key cryptography
class Sender:
    def __init__(self, cryptography, key):
        self.cryptography = cryptography
        self.publicKey = key

    # we can encrypt m by public key.
    def encrypt(self, m):
        return self.cryptography.encrypt(self.publicKey, m)

    def __str__(self):
        return 'Sender:' + \
               '\n    Cryptography='+str(self.cryptography) + \
               '\n    public key='+str(self.publicKey)
