"""Controler para RegisterCountries"""
from typing import Type
from src.domain.usecases import RegisterCountryInterface as RegisterCountry
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.interface import ControllerInterface


class RegisterCountriesController(ControllerInterface):
    """Classe para definir rotas para o caso de uso RegisterCountries"""

    def __init__(self, register_country_usecase: Type[RegisterCountry]) -> None:
        self.register_country_usecase = register_country_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = self.register_country_usecase.register_countries()

        return HttpResponse(status_code=200, body=response["data"])
