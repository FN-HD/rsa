# this is key for encryption.
class Key:
    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def __str__(self):
        return 'key:'+str(self.key)


# this is cryptography abstract class
class Cryptography:
    # convert list to string.
    @staticmethod
    def chrlist(i):
        return ''.join([chr(code) for code in i])

    # encrypt message by key
    @staticmethod
    def encrypt(key, m):
        return m

    # decrypt message by key
    @staticmethod
    def decrypt(key, m):
        return m

    # get key by data
    @staticmethod
    def get_key(data):
        return [Key(data), Key(data)]
        # [public key, private key]

    # convert string to list.
    @staticmethod
    def ordstr(c):
        return [ord(i) for i in c]


