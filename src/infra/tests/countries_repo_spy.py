"""Diretório de mocks de dados"""
from typing import List
from src.domain.models import Country
from src.domain.tests import mock_countries


class CountryRepoSpy:
    """Spy para a classe CountryRepo"""

    def __init__(self) -> None:
        self.insert_country_params = {}
        self.get_countries_params = {}

    def insert_country(self, name: str) -> Country:
        """Mock para insert_country"""

        self.insert_country_params["name"] = name

        return mock_countries()

    def get_countries(self, name: str = None) -> List[Country]:
        """Mock para get_countries"""

        self.get_countries_params["name"] = name
        return [mock_countries()]
