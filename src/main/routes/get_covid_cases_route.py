"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_covid_cases_validator import get_covid_cases_validator
from src.main.adapters.request_adapter import request_adapter
from src.presenters.errors.error_controller import handler_errors
from src.main.composers.get_covid_cases_composer import (
    get_covid_cases_composer,
)

covid_cases_routes = APIRouter(prefix="/api/covid_cases")


@covid_cases_routes.get("/")
async def get_covid_cases(request: RequestFastApi):
    """Rota para buscar os casos de covid cadastrados no banco de dados"""

    response = None

    try:
        get_covid_cases_validator(request)
        controller = get_covid_cases_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )
