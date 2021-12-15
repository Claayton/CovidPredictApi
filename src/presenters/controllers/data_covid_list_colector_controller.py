"""Diretório controlador"""
from typing import Dict, Type
from src.domain.usecases.data_covid_list_colector import DataCovidListColectorInterface


class DataCovidListColectorController:
    """Controller para listas de dados covid"""

    def __init__(self, data_covid_list_colector: Type[DataCovidListColectorInterface]) -> None:
        self.__use_case = data_covid_list_colector

    def handle(self, http_request: Dict) -> Dict:
        """Handler para listar coletores"""

        country = [http_request['query_params']['country']]
        data_covid_list = self.__use_case.list(country)
        http_response = {'status_code': 200, 'data': data_covid_list}

        return http_response
