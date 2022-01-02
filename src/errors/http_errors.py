"""Diretório para instancias error"""


class HttpErrors(Exception):
    """Classe para definir erros http"""

    @staticmethod
    def error_422():
        """Http 422"""

        return {"status_code": 422, "body": {"error": "Unprocessable Entity!"}}

    @staticmethod
    def error_400():
        """Http 400"""

        return {"status_code": 400, "body": {"error": "Bad Request!"}}
