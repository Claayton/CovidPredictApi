"""Controller para CovidCasesColector"""
from typing import Type
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.interface import ControllerInterface
from src.errors import HttpBadRequestError
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

        query_string_params = http_request.query.keys()

        if "country" not in query_string_params:
            raise HttpBadRequestError(
                message="This request need the country query-param"
            )

        country = http_request.query["country"]
        if "days" in query_string_params:
            days = http_request.query["days"]

        response = self.__use_case.covid_cases_country(country=country, days=days)

        if response["success"] is False:
            raise HttpBadRequestError(message=response["data"]["error"])

        return HttpResponse(
            status_code=200, body={"success": True, "data": response["data"]}
        )
