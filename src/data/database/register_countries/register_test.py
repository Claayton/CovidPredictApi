"""Diretório de testes para a classe RegisterCountry"""
from faker import Faker
from src.infra.tests import CountryRepoSpy, DataCovidConsumerSpy
from src.data.tests import GetCountrySpy
from .register import RegisterCountry

faker = Faker()


def test_register_country():
    """Testando o método register_country da classe RegisterCountry"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    register_countries = RegisterCountry(
        countries_repo, data_covid_consumer, get_countries
    )

    attributes = {"name": faker.name().upper()}

    response = register_countries.register_country(name=attributes["name"])

    assert countries_repo.insert_country_params["name"] == attributes["name"]

    assert response["success"] is True
    assert response["data"] is not None


def test_register_countries():
    """Testando o método register_countries da classe RegisterCountry"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    register_countries = RegisterCountry(
        countries_repo, data_covid_consumer, get_countries
    )

    response = register_countries.register_countries()

    assert countries_repo.insert_country_params is not None

    assert response["success"] is True
    assert response["data"] is not None
