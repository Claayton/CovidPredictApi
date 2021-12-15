"""Diretório Adaptador de requisições"""
from typing import Callable
from fastapi import Request as RequestFastApi

async def request_adapter(request: RequestFastApi, callback: Callable):
    """FastApi Adapter"""

    body = None
    try:
        body = await request.json()
    except:
        print('\033[31An error has occured!\033[m')

    http_request = {
        'query_params': request.query_params,
        'body': body
    }

    try:
        http_response = callback(http_request)
        return http_response
    except:
        print('\033[31An error has occured!\033[m')
