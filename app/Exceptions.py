class IncorrectCredentialsException(Exception):
    """Raise in UI only"""
    pass

class IncorrectEmailException(IncorrectCredentialsException):
    """Raise in LL only"""
    pass

class IncorrectPasswordException(IncorrectCredentialsException):
    """Raise in LL only"""
    pass

class IncorrectIdException(IncorrectCredentialsException):
    """Raise in LL only"""
    pass

class NoIdException(Exception):
    pass

class UnauthorizedRequestException(Exception):
    """Raise in LL only"""
    pass

class EmailAlreadyExistsException(Exception):
    pass

class DataNotFoundException(Exception):
    """Raise in DL only"""
    pass

class IncorrectDataException(Exception):
    """Raise in DL only"""
    pass
