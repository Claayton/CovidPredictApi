"""Diretório de inicialização do módulo errors"""
from .http_request_error import HttpRequestError
from .http_error400 import HttpBadRequestError
from .http_error404 import HttpNotFoundError
from .http_error422 import HttpUnprocessableEntityError
