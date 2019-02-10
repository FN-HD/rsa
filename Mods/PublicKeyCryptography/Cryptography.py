from Mods.PublicKeyCryptography.Key import Key

class Cryptography:
    @staticmethod
    def crypt(key, m):
        return m

    @staticmethod
    def decrypt(key, m):
        return m

    @staticmethod
    def get_key(data):
        return (Key(data), Key(data))
