"""Diretório de mocks para tests"""
from faker import Faker
from src.domain.models import Country

faker = Faker()


def mock_countries() -> Country:
    """Mock Country"""

    return Country(id=faker.random_number(digits=5), name=faker.name())
