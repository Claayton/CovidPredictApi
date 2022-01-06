"""Diretório controlador"""
from typing import Dict, Type
from src.presenters.interface.controllers import ControllersInterfaceInfo
from src.domain.usecases.covid_cases_colector_interface import (
    CovidCasesColectorInterface,
)


class DataCovidInformationColectorController(ControllersInterfaceInfo):
    """Controller para DataCovidInformationColector"""

    def __init__(
        self,
        data_covid_information_colector: Type[CovidCasesColectorInterface],
    ) -> None:
        self.__use_case = data_covid_information_colector

    def handler(self, http_request: Dict) -> Dict:
        """Handle para informações de controle de coletor"""

        country = http_request["body"]["country"]
        time = http_request["body"]["time"]

        data_covid_information = self.__use_case.find_country(country, time)
        http_response = {"status_code": 200, "data": data_covid_information}
        return http_response
