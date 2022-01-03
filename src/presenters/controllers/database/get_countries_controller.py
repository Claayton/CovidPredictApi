"""Controllers para GetCountry"""
from typing import Type
from src.domain.usecases import GetCountriesInterface as GetCountries
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpErrors


class GetCountryController:
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

            else:
                response = self.get_countries_usecase.all_countries()

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