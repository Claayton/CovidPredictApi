"""Lógica para tratamentos de erros"""
from typing import Type, Dict
from src.presenters.helpers.http_models import HttpResponse
from src.errors import (
    HttpRequestError,
    HttpBadRequestError,
    HttpUnprocessableEntityError,
)


def handler_errors(error: Type[Exception]) -> Dict:
    """
    Handler para tratamentos de exeções.
    :param error: Tipo de error gerado.
    :return: Um dicionário com o status_code e uma mensagem para esse tipo de erro.
    """

    if isinstance(
        error, (HttpRequestError, HttpBadRequestError, HttpUnprocessableEntityError)
    ):
        http_response = HttpResponse(
            status_code=error.status_code, body={"error": error.message}
        )

    else:
        http_response = HttpResponse(status_code=500, body={"error": str(error)})

    return http_response
