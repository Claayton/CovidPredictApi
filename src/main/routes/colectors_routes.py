"""Diretório de rotas do app"""

from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.main.adapters.request_adapter import request_adapter
from src.presenters.errors.error_controller import handler_errors
from src.infra.tests import CountryRepoSpy, CovidCasesRepoSpy, DataCovidConsumerSpy
from src.main.composers import (
    register_countries_composer,
    covid_cases_colector_composer,
    register_covid_cases_composer,
)
from .tests import middleware_testing

colectors = APIRouter(prefix="/api/colectors", tags=["colectors"])


@colectors.get("/covid_cases/direct/")
async def covid_cases_colector(request: RequestFastApi):
    """Rota para buscar os dados de covid no mundo e registrar no DB."""

    response = None

    try:

        if middleware_testing(request):

            controller = covid_cases_colector_composer(
                infra=DataCovidConsumerSpy(), countries_repo=CountryRepoSpy()
            )

        else:

            controller = covid_cases_colector_composer()

        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@colectors.get("/countries/")
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


@colectors.get("/covid_cases/")
async def register_covid_cases(request: RequestFastApi):
    """Rota para registrar novos casos de covid vindos da API para o banco de dados"""

    response = None

    try:

        if middleware_testing(request):

            controller = register_covid_cases_composer(
                infra_repository_countries=CountryRepoSpy(),
                infra_repository_covid_cases=CovidCasesRepoSpy(),
                infra_consumer=DataCovidConsumerSpy(),
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = register_covid_cases_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )
