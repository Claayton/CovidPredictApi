"""Diretório de mocks de dados"""
from typing import Dict
from collections import namedtuple
from faker import Faker

fake = Faker()


def mock_data_covid() -> Dict:
    """
    Mock de dados do covid
    :return: Um dicionario com as informações do covid
    """

    return {
        "BRA": [
            {
                "id": 1,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "BRA",
            }
        ],
        "USA": [
            {
                "id": 2,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "USA",
            }
        ],
        "ARG": [
            {
                "id": 3,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "ARG",
            }
        ],
    }


class DataCovidConsumerSpy:
    """Spy para DataCovidConsumer"""

    def __init__(self) -> None:
        self.get_all_data_covid_attributes = {}
        self.get_data_covid_by_country_attributes = {}
        self.get_countries_response = namedtuple(
            "GET_Countries", "status_code request response"
        )
        self.get_all_data_covid_response = namedtuple(
            "GET_Dados_covid", "status_code request response"
        )
        self.get_data_covid_by_country_response = namedtuple(
            "GET_Dados_covid_Info", "status_code request response"
        )

    def get_countries(self) -> any:
        """Mock para get_countries"""

        return self.get_countries_response(
            status_code=200, request=None, response=["BRA", "USA"]
        )

    def get_all_data_covid(self) -> any:
        """Mock para get_all_data_covid"""

        country = "BRA"

        self.get_all_data_covid_attributes["country"] = country
        return self.get_all_data_covid_response(
            status_code=200, request=None, response=mock_data_covid()
        )

    def get_data_covid_by_country(self, country: str) -> any:
        """Mock para get_data_covid_by_country"""

        country = "BRA"

        self.get_data_covid_by_country_attributes["country"] = country
        return self.get_data_covid_by_country_response(
            status_code=200, request=None, response=mock_data_covid()[country]
        )
