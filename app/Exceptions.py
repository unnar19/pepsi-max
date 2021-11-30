class IncorrectCredentialsException(Exception):
    """Raise in UI only"""
    pass

class IncorrectUsernameException(IncorrectCredentialsException):
    """Raise in LL only"""
    pass

class IncorrectPasswordException(IncorrectCredentialsException):
    """Raise in LL only"""
    pass

class IncorrectIdException(IncorrectCredentialsException):
    """Raise in LL only"""
    pass

class UnauthorizedReguestException(Exception):
    """Raise in LL only"""
    pass
