"""Controller para CovidCasesColector"""
from typing import Type
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.interface import ControllerInterface
from src.errors import HttpErrors
from src.domain.usecases import CovidCasesColectorInterface


class CovidCasesColectorController(ControllerInterface):
    """Controller para CovidCasesColector"""

    def __init__(
        self,
        covid_cases_colector: Type[CovidCasesColectorInterface],
    ) -> None:
        self.__use_case = covid_cases_colector

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None
        country = None
        days = 0

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "country" in query_string_params:
                country = http_request.query["country"]
            if "days" in query_string_params:
                days = http_request.query["days"]

            if country:
                response = self.__use_case.covid_cases_country(
                    country=country, days=days
                )

            else:
                response = self.__use_case.covid_cases_world(days=days)

            if response["success"] is True:
                return HttpResponse(status_code=200, body={"success": True})

            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
