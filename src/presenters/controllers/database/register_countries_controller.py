"""Controler para RegisterCountry"""
from typing import Type
from src.domain.usecases import RegisterCountryInterface as RegisterCountry
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpErrors


class RegisterCountryController:
    """Classe para definir rotas para o caso de uso RegisterCountry"""

    def __init__(self, register_country_usecase: Type[RegisterCountry]) -> None:
        self.register_country_usecase = register_country_usecase

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()

            if "name" in body_params:
                name = http_request.body["name"]

                response = self.register_country_usecase.register_country(name=name)

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
