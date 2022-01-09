"""Diretório de mocks para tests"""
from faker import Faker
from src.domain.models import CovidCases

faker = Faker()


def mock_covid_cases() -> CovidCases:
    """Mock CovidCases"""

    return [
        CovidCases(
            id=faker.random_number(digits=5),
            date=faker.date(),
            new_cases=faker.random_number(digits=5),
            country_id=1,
        ),
        CovidCases(
            id=faker.random_number(digits=5),
            date=faker.date(),
            new_cases=faker.random_number(digits=5),
            country_id=1,
        ),
        CovidCases(
            id=faker.random_number(digits=5),
            date=faker.date(),
            new_cases=faker.random_number(digits=5),
            country_id=1,
        ),
    ]
