"""Mocks de dados de resposta da API"""
from typing import Dict
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
            },
            {
                "id": 2,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "BRA",
            },
        ],
        "USA": [
            {
                "id": 3,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "USA",
            },
            {
                "id": 4,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "USA",
            },
        ],
        "ARG": [
            {
                "id": 5,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "ARG",
            },
            {
                "id": 5,
                "date": fake.date(),
                "new_cases": fake.random_int(),
                "country": "ARG",
            },
        ],
    }
