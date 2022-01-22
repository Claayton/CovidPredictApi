"""Alteração do estado da rota para testes"""
from xmlrpc.client import Boolean
from fastapi import Request as RequestFastApi


def middleware_testing(request: RequestFastApi) -> Boolean:
    """
    Verifica se existe o header X-Tests = True no header da requisição.
    :param request: Objeto de requisições que vai receber o header.
    :return: True caso o header exista, ou False caso contrário.
    """

    headers = request.headers

    if "X-Test" in headers:

        return True

    return False
