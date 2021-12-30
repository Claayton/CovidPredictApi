"""Diretório de mocks de dados"""
from typing import List, Tuple
from src.domain.models import CovidCases
from src.domain.tests import mock_covid_cases


class CovidCasesRepoSpy:
    """Spy para a classe CovidCasesRepo"""

    def __init__(self) -> None:
        self.insert_data_params = {}
        self.get_covid_cases_params = {}

    def insert_data(self, data_date: str, new_cases: int, country: str) -> CovidCases:
        """Mock para insert_data"""

        self.insert_data_params["data_date"] = data_date
        self.insert_data_params["new_cases"] = new_cases
        self.insert_data_params["country"] = country

        return mock_covid_cases()

    def get_data(self, country: str = None, data_date: str = None) -> List[Tuple]:
        """Mock para get_data"""

        self.get_covid_cases_params["country"] = country
        self.get_covid_cases_params["data_date"] = data_date

        return [mock_covid_cases()]
