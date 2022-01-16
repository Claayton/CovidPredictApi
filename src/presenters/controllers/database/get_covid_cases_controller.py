"""Controllers para GetCovidCases"""
from typing import Type, List
from datetime import date
from src.domain.models.covid_cases import CovidCases
from src.domain.usecases import GetCovidCasesInterface as GetCovidCases
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpBadRequestError, HttpUnprocessableEntityError
from src.presenters.interface import ControllerInterface


class GetCovidCasesController(ControllerInterface):
    """Classe que define controller para o caso de uso: GetCovidCases"""

    def __init__(self, get_covid_cases_usecase: Type[GetCovidCases]) -> None:
        self.get_covid_cases_usecase = get_covid_cases_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if ("date" in query_string_params) and ("country" in query_string_params):
                data_date = http_request.query["date"]
                country = http_request.query["country"]
                response = self.get_covid_cases_usecase.by_country_and_by_date(
                    country=country, data_date=data_date
                )

            elif ("date" in query_string_params) and (
                "country" not in query_string_params
            ):

                data_date = http_request.query["date"]
                response = self.get_covid_cases_usecase.by_date(data_date=data_date)

            elif ("date" not in query_string_params) and (
                "country" in query_string_params
            ):

                country = http_request.query["country"]
                response = self.get_covid_cases_usecase.by_country(country=country)

            if response["success"] is False:
                raise HttpUnprocessableEntityError(message="Invalid country or date!")

            return self.__formated_response(response["data"])

        response = self.get_covid_cases_usecase.by_country(country="WORLD")

        if response["success"] is False:
            raise HttpBadRequestError(
                message="This request need 1 of 2 query-params: (country: str) or (date: str(aaaa-mm-dd))"
            )

        return self.__formated_response(response["data"])

    @classmethod
    def __formated_response(
        cls, usecase_response: List[CovidCases]
    ) -> List[CovidCases]:

        if usecase_response is not None:

            response = []

            for data in usecase_response:

                response.append(
                    {
                        "id": data.id,
                        "date": date.isoformat(data.date),
                        "new_cases": data.new_cases,
                        "country_id": data.country_id,
                    }
                )

            return HttpResponse(status_code=200, body=response)

        raise HttpUnprocessableEntityError()
