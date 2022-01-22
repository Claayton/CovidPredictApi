"""Controler para RegisterCountry"""
from typing import Type
from src.domain.usecases import RegisterCountryInterface as RegisterCountry
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpUnprocessableEntityError, HttpBadRequestError
from src.presenters.interface import ControllerInterface


class RegisterCountryController(ControllerInterface):
    """Classe para definir rotas para o caso de uso RegisterCountry"""

    def __init__(self, register_country_usecase: Type[RegisterCountry]) -> None:
        self.register_country_usecase = register_country_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()

            if "name" not in body_params:
                raise HttpUnprocessableEntityError(
                    message="This request need the name body-param"
                )
            name = http_request.body["name"]

            response = self.register_country_usecase.register_country(name=name)

            return HttpResponse(status_code=200, body=response["data"])

        raise HttpBadRequestError(message="This request need the name body-param")
