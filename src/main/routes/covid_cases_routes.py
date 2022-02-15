"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.infra.tests import CountryRepoSpy, CovidCasesRepoSpy, DataCovidConsumerSpy
from src.main.adapters.request_adapter import request_adapter
from src.presenters.errors.error_controller import handler_errors
from src.validators import get_covid_cases_validator, covid_cases_predict_validator
from src.main.composers import (
    get_covid_cases_composer,
    covid_cases_predict_composer,
    covid_cases_colector_composer,
    register_covid_cases_composer,
)
from .tests import middleware_testing

covid_cases = APIRouter(prefix="/api/covid_cases")


@covid_cases.get("/", tags=["covid_cases"])
async def get_covid_cases(request: RequestFastApi):
    """Rota para buscar os casos de covid cadastrados no banco de dados"""

    response = None

    try:

        get_covid_cases_validator(request)

        if middleware_testing(request):

            controller = get_covid_cases_composer(
                infra=CovidCasesRepoSpy(), countries_repo=CountryRepoSpy()
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = get_covid_cases_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@covid_cases.post("/", tags=["covid_cases"])
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


@covid_cases.get("/predict", tags=["predict"])
async def covid_cases_predict(request: RequestFastApi):
    """Rota para buscar os dados de covid no mundo e registrar no DB."""

    response = None

    try:

        covid_cases_predict_validator(request)

        if middleware_testing(request):

            controller = covid_cases_predict_composer(infra=CovidCasesRepoSpy())
            response = await request_adapter(request, controller.handler)

        else:

            controller = covid_cases_predict_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@covid_cases.get("/colector", tags=["colector"])
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
