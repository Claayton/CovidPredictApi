"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_covid_cases_validator import get_covid_cases_validator
from src.main.adapters.request_adapter import request_adapter
from src.errors.http_errors import HttpErrors
from src.main.composers.get_covid_cases_composer import (
    get_covid_cases_composer,
)

covid_cases_routes = APIRouter()


@covid_cases_routes.get("/api/covid_cases/")
async def get_data_covid_from_country(request: RequestFastApi):
    """Rota para buscar os casos de covid cadastrados no sistema"""

    try:
        get_covid_cases_validator(request)
    except Exception as error:  # pylint: disable=W0703
        http_error = HttpErrors.error_400()
        return JSONResponse(
            status_code=http_error["status_code"], content={"error": str(error)}
        )

    controller = get_covid_cases_composer()
    response = await request_adapter(request, controller.handler)

    return JSONResponse(status_code=response.status_code, content=response.body)
