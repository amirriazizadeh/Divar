from user import User
from my_exceptions import *

class Authenticator:
    def __init__(self):
        self.users = {}

    def signup(self, username: str, password: str):
        if username in self.users:
            raise UsernameAlreadyExists("Username already exists.")
        if len(password) < 8:
            raise PasswordTooShort("Password must be at least 8 characters.")
        
        self.users[username] = User(username, password)
        print(f"User '{username}' signed up successfully.")

    def login(self, username: str, password: str):
        if username not in self.users:
            raise InvalidUsername("Username does not exist.")
        
        user = self.users[username]
        if not user.check_password(password):
            raise InvalidPassword("Incorrect password.")
        
        user.logged_in = True
        print(f"User '{username}' logged in successfully.")

    def logout(self, username: str):
        if username in self.users and self.users[username].logged_in:
            self.users[username].logged_in = False
            print(f"User '{username}' logged out.")
        else:
            print("User is not logged in.")

    def is_logged_in(self, username: str) -> bool:
        return self.users.get(username).logged_in if username in self.users else False





auth = Authenticator()

try:
    auth.signup("ali", "123") 
except AuthException as e:
    print("Error:", e)

try:
    auth.signup("ali", "12345678")
    auth.signup("ali", "87654321") 
except AuthException as e:
    print("Error:", e)

try:
    auth.login("reza", "12345678") 
except AuthException as e:
    print("Error:", e)

try:
    auth.login("ali", "wrongpass")  
except AuthException as e:
    print("Error:", e)

auth.login("ali", "12345678")
print("is_logged_in:", auth.is_logged_in("ali"))
auth.logout("ali")
