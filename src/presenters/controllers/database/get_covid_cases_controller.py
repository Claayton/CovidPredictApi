"""Controllers para GetCovidCases"""
from typing import Type
from src.domain.usecases import GetCovidCasesInterface as GetCovidCases
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpErrors


class GetCovidCasesController:
    """Classe que define controller para o caso de uso: GetCovidCases"""

    def __init__(self, get_covid_cases_usecase: Type[GetCovidCases]) -> None:
        self.get_covid_cases_usecase = get_covid_cases_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if ("date" in query_string_params) and ("country" in query_string_params):
                date = http_request.query["date"]
                country = http_request.query["country"]
                response = self.get_covid_cases_usecase.by_country_and_by_date(
                    country=country, data_date=date
                )

            elif ("date" in query_string_params) and (
                "country" not in query_string_params
            ):
                date = http_request.query["date"]
                response = self.get_covid_cases_usecase.by_date(data_date=date)

            elif ("date" not in query_string_params) and (
                "country" in query_string_params
            ):
                country = http_request.query["country"]
                response = self.get_covid_cases_usecase.by_country(country=country)

            else:
                response = {"success": False, "data": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
