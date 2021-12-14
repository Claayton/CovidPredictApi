"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from src.validators.get_data_covid_from_country_validator import get_from_country_validator
from src.main.adapters.request_adapter import request_adapter

data_covid_routes = APIRouter()

@data_covid_routes.get("/api/datacovid/list")
async def get_data_covid_from_country(request: RequestFastApi):
    """Get_data_covid_from_country"""

    get_from_country_validator(request)
    await request_adapter(request, print)

    return {"Ola": "Mundo!"}
 