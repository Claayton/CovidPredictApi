"""Diretório de testes para a classe RegisterCountry"""
from faker import Faker
from src.infra.tests import CountryRepoSpy, DataCovidConsumerSpy
from .register import RegisterCountry

faker = Faker()


def test_register_country():
    """Testando o método register_country da classe RegisterCountry"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_countries = RegisterCountry(countries_repo, data_covid_consumer)

    attributes = {"name": faker.name().upper()}

    response = register_countries.register_country(name=attributes["name"])

    assert countries_repo.insert_country_params["name"] == attributes["name"]

    assert response["success"] is True
    assert response["data"] is not None


def test_register_country_fail():
    """Testando o erro no método register_country da classe RegisterCountry"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_country = RegisterCountry(countries_repo, data_covid_consumer)

    attributes = {"name": faker.random_number(digits=2)}

    response = register_country.register_country(name=attributes["name"])

    assert countries_repo.insert_country_params == {}

    assert response["success"] is False
    assert response["data"] is None


def test_register_countries():
    """Testando o método register_countries da classe RegisterCountry"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_countries = RegisterCountry(countries_repo, data_covid_consumer)

    response = register_countries.register_countries()

    assert countries_repo.insert_country_params is not None

    assert response["success"] is True
    assert response["data"] is not None
