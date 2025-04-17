import hashlib

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.logged_in = False

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password_hash == self._hash_password(password)
