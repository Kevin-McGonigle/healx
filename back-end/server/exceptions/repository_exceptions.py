class RepositoryException(Exception):
    pass


class EntityNotFoundException(RepositoryException):
    def __init__(self, message: str):
        super().__init__(message)
