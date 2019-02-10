class Key:
    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def __str__(self):
        return 'key:'+str(self.key)