"""Diretório de rotas do app"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.infra.tests import DataCovidConsumerSpy
from src.presenters.errors.error_controller import handler_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers import covid_cases_colector_composer
from .tests import middleware_testing

covid_cases_colector_routes = APIRouter(prefix="/api/colector")


@covid_cases_colector_routes.get("/")
async def colector(request: RequestFastApi):
    """Rota para buscar os dados de covid no mundo e registrar no DB."""

    response = None

    try:

        if middleware_testing(request):

            infra = DataCovidConsumerSpy()
            controller = covid_cases_colector_composer(infra=infra)
        else:

            controller = covid_cases_colector_composer()

        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )
