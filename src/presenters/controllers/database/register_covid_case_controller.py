"""Controler para RegisterCovidCase"""
from typing import Type
from src.presenters.helpers import HttpRequest, HttpResponse
from src.errors import HttpUnprocessableEntityError, HttpBadRequestError
from src.presenters.interface import ControllerInterface
from src.domain.usecases import RegisterCovidCasesInterface as RegisterCovidCases


class RegisterCovidCaseController(ControllerInterface):
    """Classe para definir rotas para o caso de uso RegisterCovidCase"""

    def __init__(self, register_covid_cases_usecase: Type[RegisterCovidCases]) -> None:
        self.__register_covid_cases_usecase = register_covid_cases_usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
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

                response = self.__register_covid_cases_usecase.register(
                    date=date, new_cases=new_cases, country=country
                )

                return HttpResponse(status_code=200, body=response["data"])

            raise HttpUnprocessableEntityError(
                message="""
                This request need 3 query-params: (date: str(aaaa-mm-dd)), (new_cases: int), (country: str)
                """
            )
        raise HttpBadRequestError(
            message="""
            "This request need 3 query-params: (date: str(aaaa-mm-dd)), (new_cases: int), (country: str)
            """
        )
