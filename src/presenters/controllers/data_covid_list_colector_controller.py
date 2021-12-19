"""Diretório controlador"""
from typing import Dict, Type
from src.presenters.interface.controllers import ControllersInterfaceList
from src.domain.usecases.data_covid_list_colector import DataCovidListColectorInterface


class DataCovidListColectorController(ControllersInterfaceList):
    """Controller para listas de dados covid"""

    def __init__(
        self, data_covid_list_colector: Type[DataCovidListColectorInterface]
    ) -> None:
        self.__use_case = data_covid_list_colector

    def handler(self) -> Dict:
        """Handler para listar coletores"""

        data_covid_list = self.__use_case.list()
        http_response = {"status_code": 200, "data": data_covid_list}

        return http_response
