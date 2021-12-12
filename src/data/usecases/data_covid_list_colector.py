"""Diretório para Dominio e casos de uso"""
from typing import Dict, Type
from src.domain.usecases import DataCovidListColectorInterface
from src.data.interfaces.data_covid_consumer import DataCovidConsumerInterface


class DataCovidListColector(DataCovidListColectorInterface):
    """Casos de uso para DataCovidListColector"""

    def __init__(self, api_consumer: Type[DataCovidConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self) -> Dict:
        response = self.__api_consumer.get_data_covid()
        print(response)
