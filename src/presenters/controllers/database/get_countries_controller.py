"""Controllers para GetCountry"""
from typing import Type, List
from src.domain.usecases import GetCountriesInterface as GetCountries
from src.domain.models import Country
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import (
    HttpUnprocessableEntityError,
    HttpBadRequestError,
    HttpNotFoundError,
)
from src.presenters.interface import ControllerInterface


class GetCountryController(ControllerInterface):
    """Classe que define controller para o caso de uso: GetCountry"""

    def __init__(self, get_countries_usecase: Type[GetCountries]) -> None:
        self.get_countries_usecase = get_countries_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "name" in query_string_params:
                country_name = http_request.query["name"]
                response = self.get_countries_usecase.by_name(name=country_name)

                if response["success"] is False:
                    raise HttpUnprocessableEntityError(message="Invalid Country!")

                return self.__formated_response(response["data"])

        response = self.get_countries_usecase.all_countries()

        if response["success"] is False:
            raise HttpBadRequestError()

        return self.__formated_response(response["data"])

    @classmethod
    def __formated_response(cls, usecase_response: List[Country]) -> List[Country]:

        if usecase_response == []:

            raise HttpNotFoundError(message="No data found in the database.")

        response = []

        for data in usecase_response:

            response.append({"id": data.id, "name": data.name})

        return HttpResponse(status_code=200, body=response)
