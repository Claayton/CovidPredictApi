"""Controler para RegisterAllCovidCases"""
from typing import Type
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.interface import ControllerInterface
from src.domain.usecases import RegisterCovidCasesInterface as RegisterCovidCases


class RegisterCovidCasesController(ControllerInterface):
    """Classe para definir rotas para o caso de uso RegisterCovidCases"""

    def __init__(self, register_covid_cases_usecase: Type[RegisterCovidCases]) -> None:
        self.__register_covid_cases_usecase = register_covid_cases_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = self.__register_covid_cases_usecase.register_covid_cases()

        return HttpResponse(status_code=200, body=response["data"])
