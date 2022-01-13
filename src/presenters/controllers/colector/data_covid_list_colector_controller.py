"""Diretório controlador"""
from typing import Dict, Type
from src.presenters.interface.controllers_interface import ControllersInterfaceList
from src.domain.usecases.covid_cases_predict_interface import (
    CovidCasesPredictInterface as CovidCasesPredict,
)


class DataCovidListColectorController(ControllersInterfaceList):
    """Controller para listas de dados covid"""

    def __init__(self, data_covid_list_colector: Type[CovidCasesPredict]) -> None:
        self.__use_case = data_covid_list_colector

    def handler(self) -> Dict:
        """Handler para listar coletores"""

        data_covid_list = self.__use_case.list()
        http_response = {"status_code": 200, "data": data_covid_list}

        return http_response
