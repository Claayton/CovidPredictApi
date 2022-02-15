"""Diretório para instancias error"""


class HttpNotFoundError(Exception):
    """HttpError 404 - (Not Found!)"""

    def __init__(self, message: str = "Not Found!") -> None:
        super().__init__(message)
        self.message = message
        self.name = "NotFoundError"
        self.status_code = 404
