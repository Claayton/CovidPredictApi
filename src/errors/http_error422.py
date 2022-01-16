"""Diretório para instancias error"""


class HttpUnprocessableEntityError(Exception):
    """HttpError 422 - (Unprocessable Entity!)"""

    def __init__(self, message: str = "Unprocessable Entity!") -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntityError"
        self.status_code = 422
