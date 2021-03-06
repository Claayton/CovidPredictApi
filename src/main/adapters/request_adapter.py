"""Diretório Adaptador de requisições"""
from typing import Callable
from fastapi import Request as RequestFastApi
from src.presenters.helpers import HttpRequest


async def request_adapter(request: RequestFastApi, callback: Callable):
    """FastApi Adapter"""

    body = None
    try:
        body = await request.json()
    except:  # pylint: disable=W0702
        pass

    http_request = HttpRequest(body=body, query=request.query_params)

    http_response = callback(http_request)
    return http_response
