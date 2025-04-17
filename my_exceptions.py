# exceptions.py

class AuthException(Exception):
    """Base class for authentication exceptions."""
    pass

class UsernameAlreadyExists(AuthException):
    """Raised when the username already exists during signup."""
    pass

class PasswordTooShort(AuthException):
    """Raised when the password is too short."""
    pass

class InvalidUsername(AuthException):
    """Raised when the username is not found during login."""
    pass

class InvalidPassword(AuthException):
    """Raised when the password is incorrect during login."""
    pass
