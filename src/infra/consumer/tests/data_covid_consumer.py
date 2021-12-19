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
    return [
        {
            "id": 1,
            "date": fake.date(),
            "new_cases": fake.random_int(),
            "country": "BRA",
        },
        {
            "id": 2,
            "date": fake.date(),
            "new_cases": fake.random_int(),
            "country": "BRA",
        },
        {
            "id": 3,
            "date": fake.date(),
            "new_cases": fake.random_int(),
            "country": "BRA",
        },
        {
            "id": 4,
            "date": fake.date(),
            "new_cases": fake.random_int(),
            "country": "BRA",
        },
        {
            "id": 5,
            "date": fake.date(),
            "new_cases": fake.random_int(),
            "country": "BRA",
        },
    ]


class DataCovidConsumerSpy:
    """Spy para DataCovidConsumer"""

    def __init__(self) -> None:
        self.get_data_covid_attributes = {}
        self.get_data_covid_information_attributes = {}
        self.get_data_covid_response = namedtuple(
            "GET_Dados_covid", "status_code request response"
        )
        self.get_data_covid_information_response = namedtuple(
            "GET_Dados_covid_Info", "status_code request response"
        )

    def get_data_covid(self) -> any:
        """Mock para get_data_covid"""

        country = ["BRA"]

        self.get_data_covid_attributes["country"] = country
        return self.get_data_covid_response(
            status_code=200,
            request=None,
            response={country[0]: {"data": [mock_data_covid()[0]]}},
        )

    def get_data_covid_information(self, country: str) -> any:
        """Mock para get_data_covid"""

        country = "BRA"

        self.get_data_covid_information_attributes["country"] = country
        return self.get_data_covid_response(
            status_code=200, request=None, response=mock_data_covid()
        )
