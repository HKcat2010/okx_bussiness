class user:
    def __init__(self, key, secret, passphrase):
        self.key = key
        self.secret = secret
        self.passphrase = passphrase

    def get_credentials(self):
        return {
            "key": self.key,
            "secret": self.secret,
            "passphrase": self.passphrase
        }