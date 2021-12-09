### DATA

class DataLayerException(Exception):
    def __init__(self, key: str, method: str, type: str) -> None:
        self.class_ = key
        self.method = method
        self.type = type

    def __str__(self) -> str:
        return f'{self.type}: method {self.method} failed in {self.class_} database'

class DatabaseEmptyException(DataLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'DatabaseEmpty')

    def __str__(self) -> str:
        return super().__str__()

class IncorrectDataException(DataLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'IncorrectData')

    def __str__(self) -> str:
        return super().__str__()

### LOGIC

class LogicLayerException(Exception):
    def __init__(self, key: str, method: str, type: str) -> None:
        self.class_ = key
        self.method = method
        self.type = type

    def __str__(self) -> str:
        return f'{self.type}: method {self.method} failed in {self.class_} backend'

class DataAlreadyExistsException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'DataAlreadyExists')

    def __str__(self) -> str:
        return super().__str__()

class UnauthorizedRequestException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'UnauthorizedRequest')

    def __str__(self) -> str:
        return super().__str__()

class IncorrectIdException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'IncorrectID')

    def __str__(self) -> str:
        return super().__str__()

class IncorrectCredentialsException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'IncorrectCredentials')

    def __str__(self) -> str:
        return super().__str__()

class NoIdException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'NoID')

    def __str__(self) -> str:
        return super().__str__()

class IncorrectInputException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'IncorrectInput')

    def __str__(self) -> str:
        return super().__str__()

class NotFoundException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'NotFound')

    def __str__(self) -> str:
        return super().__str__()

class IncorrectFieldsException(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'IncorrectFields')

    def __str__(self) -> str:
        return super().__str__()

class Un(LogicLayerException):
    def __init__(self, key: str, method: str) -> None:
        super().__init__(key, method, 'IncorrectFields')

    def __str__(self) -> str:
        return super().__str__()