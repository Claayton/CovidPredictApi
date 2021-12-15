"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.validators.get_data_covid_from_country_validator import get_from_country_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_data_covid_from_country_composer import (
    get_data_covid_from_country_composer
)

data_covid_routes = APIRouter()

@data_covid_routes.get("/api/datacovid/list")
async def get_data_covid_from_country(request: RequestFastApi):
    """Get_data_covid_from_country"""

    get_from_country_validator(request)
    controller = get_data_covid_from_country_composer()

    response = await request_adapter(request, controller.handle)

    return JSONResponse(
        status_code=response['status_code'],
        content={"data": response['data']}
    )
