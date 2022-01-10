"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_countries_validator import get_from_country_validator
from src.main.adapters.request_adapter import request_adapter
from src.errors.http_errors import HttpErrors
from src.main.composers.get_countries_composer import get_countries_composer

countries_routes = APIRouter()


@countries_routes.get("/api/countries/")
async def get_countries(request: RequestFastApi):
    """Rota para buscar os países cadastrados no sistema"""

    try:
        get_from_country_validator(request)
    except:
        http_error = HttpErrors.error_400()
        return JSONResponse(
            status_code=http_error["status_code"], content=http_error["body"]
        )

    controller = get_countries_composer()
    response = await request_adapter(request, controller.handler)

    return JSONResponse(status_code=response.status_code, content=response.body)


# Essa rota fica melhor com get!
# @data_covid_routes.post("/api/datacovid/information/")
# async def get_data_covid_information(request: RequestFastApi):
#     """Get_data_covid_information"""

#     controller = get_data_covid_information_composer()

#     response = await request_adapter(request, controller.handler)
#     print(f'\033[34m{response["data"]}\033[m')

#     return JSONResponse(status_code=response["status_code"], content=response["data"])