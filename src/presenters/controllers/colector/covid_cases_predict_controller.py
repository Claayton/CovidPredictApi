"""Controller para CovidCasesPredict"""
from typing import Type
from src.presenters.interface import ControllerInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpErrors
from src.domain.usecases.covid_cases_predict_interface import (
    CovidCasesPredictInterface as CovidCasesPredict,
)


class CovidCasesPredictController(ControllerInterface):
    """Controller para CovidCasesPredict"""

    def __init__(self, covid_cases_predict: Type[CovidCasesPredict]) -> None:
        self.__use_case = covid_cases_predict

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Handler para listar coletores"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if (
                "country" not in query_string_params
                or "days" not in query_string_params
            ):

                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            else:
                country = http_request.query["country"]
                days = http_request.query["days"]

                response = self.__use_case.covid_evolution_predict(
                    country=country, days=days
                )

            if response["success"] is True:
                return HttpResponse(status_code=200, body=response)

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
