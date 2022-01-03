"""Diretório de interface de consumo da API"""
from abc import ABC, abstractmethod
from typing import Type, Tuple, Dict, List
from requests import Request


class DataCovidConsumerInterface(ABC):
    """Interface de consumo de API"""

    @abstractmethod
    def get_countries(self) -> Tuple[int, Type[Request], List]:
        """Deve ser implementado"""
        raise Exception("Must implement get_data_covid")

    @abstractmethod
    def get_all_data_covid(self) -> Tuple[int, Type[Request], Dict]:
        """Deve ser implementado"""
        raise Exception("Must implement get_data_covid")

    @abstractmethod
    def get_data_covid_information(
        self, country: str
    ) -> Tuple[int, Type[Request], Dict]:
        """Deve ser implementado"""
        raise Exception("Must implement get_data_covid_information")
