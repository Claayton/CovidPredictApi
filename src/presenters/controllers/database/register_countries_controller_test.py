"""Testes para a classe RegisterCountriesController"""
from faker import Faker
from src.data.tests import RegisterCountriesSpy
from src.infra.tests import CountryRepoSpy, DataCovidConsumerSpy
from . import RegisterCountriesController

faker = Faker()


def test_handler():
    """Testando o método handler"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_countries_usecase = RegisterCountriesSpy(
        countries_repo, data_covid_consumer
    )
    register_countries_controller = RegisterCountriesController(
        register_countries_usecase
    )

    response = register_countries_controller.handler(None)

    assert response.status_code == 200
    assert "error" not in response.body
