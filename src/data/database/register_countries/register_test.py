"""Testes para a classe RegisterCountries"""
from faker import Faker
from src.infra.tests import CountryRepoSpy, DataCovidConsumerSpy
from src.data.tests import GetCountrySpy
from .register import RegisterCountries

faker = Faker()


def test_register_countries():
    """Testando o método register_countries da classe RegisterCountries"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    register_countries = RegisterCountries(
        countries_repo, data_covid_consumer, get_countries
    )

    response = register_countries.register_countries()

    # Testando a entrada:
    assert countries_repo.insert_country_params is not None

    # Testando a saída:
    assert response["success"] is True
    assert response["data"] is not None
