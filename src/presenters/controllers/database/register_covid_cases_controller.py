"""Controler para RegisterCovidCases"""
from typing import Type
from src.domain.usecases import RegisterCovidCasesInterface as RegisterCovidCases
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpErrors


class RegisterCoviCasesController:
    """Classe para definir rotas para o caso de uso RegisterCoviCases"""

    def __init__(self, register_covid_cases_usecase: Type[RegisterCovidCases]) -> None:
        self.register_covid_cases_usecase = register_covid_cases_usecase

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Método para chamar o caso de uso"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()

            if (
                "date" in body_params
                and "new_cases" in body_params
                and "country" in body_params
            ):
                date = http_request.body["date"]
                new_cases = http_request.body["new_cases"]
                country = http_request.body["country"]

                response = self.register_covid_cases_usecase.register(
                    date=date, new_cases=new_cases, country=country
                )

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
