"""Testes para a classe RegisterCountryController"""
from faker import Faker
from src.data.tests import RegisterCountrySpy
from src.infra.tests import CountryRepoSpy, DataCovidConsumerSpy
from src.presenters.helpers import HttpRequest
from . import RegisterCountryController

faker = Faker()


def test_route():
    """Testando o método route"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_countries_usecase = RegisterCountrySpy(countries_repo, data_covid_consumer)
    register_countries_route = RegisterCountryController(register_countries_usecase)

    attibutes = {"name": faker.name()}

    response = register_countries_route.handler(
        http_request=HttpRequest(body=attibutes)
    )

    assert register_countries_usecase.name_params["name"] == attibutes["name"]

    assert response.status_code == 200
    assert "error" not in response.body
