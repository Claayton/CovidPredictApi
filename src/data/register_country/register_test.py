"""Diretório de testes para a classe RegisterCountry"""
from faker import Faker
from src.infra.tests import CountryRepoSpy
from .register import RegisterCountry

faker = Faker()


def test_register():
    """Testando o método register da classe RegisterCountry"""

    country_repo = CountryRepoSpy()
    register_country = RegisterCountry(country_repo)

    attributes = {"name": faker.name()}

    response = register_country.register(name=attributes["name"])

    assert country_repo.insert_country_params["name"] == attributes["name"]

    assert response["sucess"] is True
    assert response["data"]


def test_register_fail():
    """Testando o erro no método register da classe RegisterCountry"""

    country_repo = CountryRepoSpy()
    register_country = RegisterCountry(country_repo)

    attributes = {"name": faker.random_number(digits=2)}

    response = register_country.register(name=attributes["name"])

    print(response)

    assert country_repo.insert_country_params == {}

    assert response["sucess"] is False
    assert response["data"] is None
