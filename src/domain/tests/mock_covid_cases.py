"""Diretório de mocks para tests"""
from datetime import datetime
from faker import Faker
from src.domain.models import CovidCases

faker = Faker()


def mock_covid_cases() -> CovidCases:
    """Mock CovidCases"""

    return [
        CovidCases(
            id=faker.random_number(digits=5),
            date=datetime.strptime("2022-01-01", "%Y-%m-%d"),
            new_cases=faker.random_number(digits=5),
            country_id=1,
        ),
        CovidCases(
            id=faker.random_number(digits=5),
            date=datetime.strptime("2022-01-02", "%Y-%m-%d"),
            new_cases=faker.random_number(digits=5),
            country_id=1,
        ),
        CovidCases(
            id=faker.random_number(digits=5),
            date=datetime.strptime("2022-01-03", "%Y-%m-%d"),
            new_cases=faker.random_number(digits=5),
            country_id=1,
        ),
    ]
