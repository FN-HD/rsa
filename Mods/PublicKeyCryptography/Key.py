class Key:
    def get_key(self):
        return None


class PublicKey(Key):
    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key


class PrivateKey(Key):
    def __init__(self,key):
        self.key = key

    def get_key(self):
        return self.key