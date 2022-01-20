"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.main.adapters.request_adapter import request_adapter
from src.presenters.errors.error_controller import handler_errors
from src.main.composers import get_countries_composer, register_country_composer
from src.validators.countries_validator import (
    get_from_country_validator,
    register_countries_validator,
)

countries = APIRouter()


@countries.get("/api/countries/")
async def get_countries(request: RequestFastApi):
    """Rota para buscar os países cadastrados no sistema"""

    response = None

    try:
        get_from_country_validator(request)
        controller = get_countries_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@countries.post("/api/countries/")
async def register_country(request: RequestFastApi):
    """Rota para registrar um novo país no sistema"""

    response = None

    try:
        await register_countries_validator(request)
        controller = register_country_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


# @countries.post("/api/countries/")
# async def register_countries(request: RequestFastApi):
#     """Rota para registrar automáticamente novos países no sistema"""

#     response = None

#     try:
#         await register_countries_validator(request)
#         controller = register_countries_composer()
#         response = await request_adapter(request, controller.handler)

#     except Exception as error:  # pylint: disable=W0703
#         response = handler_errors(error)

#     return JSONResponse(
#         status_code=response.status_code, content={"data": response.body}
#     )
