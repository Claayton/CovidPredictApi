"""Diretório Adaptador de requisições"""
from typing import Callable
from fastapi import Request as RequestFastApi
from src.presenters.helpers import HttpRequest


async def request_adapter(request: RequestFastApi, callback: Callable):
    """FastApi Adapter"""

    body = None
    try:
        body = await request.json()
    except:
        pass

    http_request = HttpRequest(body=body, query=request.query_params)

    try:
        http_response = callback(http_request)
    except TypeError:
        http_response = callback()
    return http_response
