"""Controllers para GetCovidCases"""
from typing import Type, List
from datetime import date, datetime
from src.domain.models.covid_cases import CovidCases
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import (
    HttpBadRequestError,
    HttpUnprocessableEntityError,
    HttpRequestError,
)
from src.presenters.interface import ControllerInterface
from src.domain.usecases import (
    GetCovidCasesInterface as GetCovidCases,
    GetCountriesInterface as GetCountry,
)


class GetCovidCasesController(ControllerInterface):
    """Classe que define controller para o caso de uso: GetCovidCases"""

    def __init__(
        self,
        get_covid_cases_usecase: Type[GetCovidCases],
        get_countries_usecase: Type[GetCountry],
    ) -> None:
        self.__get_covid_cases_usecase = get_covid_cases_usecase
        self.__get_countries_usecase = get_countries_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "date" in query_string_params:

                data_date = http_request.query["date"]

                try:
                    datetime.strptime(data_date, "%Y-%m-%d")
                except ValueError as error:
                    raise HttpUnprocessableEntityError(message=str(error)) from error
                except Exception as error:
                    raise HttpBadRequestError(message=str(error)) from error

            if ("date" in query_string_params) and ("country" in query_string_params):
                data_date = http_request.query["date"]
                country = http_request.query["country"]
                response = self.__get_covid_cases_usecase.by_country_and_by_date(
                    country=country, data_date=data_date
                )

            elif ("date" in query_string_params) and (
                "country" not in query_string_params
            ):

                data_date = http_request.query["date"]
                response = self.__get_covid_cases_usecase.by_date(data_date=data_date)

            elif ("date" not in query_string_params) and (
                "country" in query_string_params
            ):

                country = http_request.query["country"]
                response = self.__get_covid_cases_usecase.by_country(country=country)

            if response["success"] is False:
                raise HttpUnprocessableEntityError(message="Invalid country or date!")

            return self.__formated_response(response["data"])

        response = self.__get_covid_cases_usecase.by_country(country="WORLD")

        if response["success"] is False:
            raise HttpBadRequestError(
                message="""
                This request need 1 of 2 query-params: (country: str) or (date: str(aaaa-mm-dd))
                """
            )

        return self.__formated_response(response["data"])

    def __formated_response(
        self, usecase_response: List[CovidCases]
    ) -> List[CovidCases]:

        if usecase_response == []:

            raise HttpRequestError(status_code=302, message="Found!")

        response = []

        for data in usecase_response:

            response.append(
                {
                    "id": data.id,
                    "date": date.isoformat(data.date),
                    "new_cases": data.new_cases,
                    "country": self.__get_country_name(data.country_id),
                }
            )

        return HttpResponse(status_code=200, body=response)

    def __get_country_name(self, country_id: int):

        country = self.__get_countries_usecase.by_id(country_id=country_id)["data"][0]
        country_name = country.name

        return country_name
