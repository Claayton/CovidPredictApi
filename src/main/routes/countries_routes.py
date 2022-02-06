"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.main.adapters.request_adapter import request_adapter
from src.presenters.errors.error_controller import handler_errors
from src.infra.tests import CountryRepoSpy, DataCovidConsumerSpy
from src.main.composers import get_countries_composer, register_countries_composer
from src.validators.countries_validator import get_from_country_validator
from .tests import middleware_testing

countries = APIRouter(prefix="/api/countries")


@countries.get("/")
async def get_countries(request: RequestFastApi):
    """Rota para buscar os países cadastrados no sistema"""

    response = None

    try:

        if middleware_testing(request):

            get_from_country_validator(request)
            controller = get_countries_composer(infra=CountryRepoSpy())

        else:

            get_from_country_validator(request)
            controller = get_countries_composer()

        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@countries.post("/")
async def register_countries(request: RequestFastApi):
    """Rota para registrar automáticamente novos países no sistema"""

    response = None

    try:

        if middleware_testing(request):

            controller = register_countries_composer(
                infra_repository=CountryRepoSpy(), infra_consumer=DataCovidConsumerSpy()
            )

        else:

            controller = register_countries_composer()

        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )
