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

    response = register_countries_route.route(http_request=HttpRequest(body=attibutes))

    assert register_countries_usecase.name_params["name"] == attibutes["name"]

    assert response.status_code == 200
    assert "error" not in response.body


def test_route_fail_422():
    """Testando o erro 400 no método route (sem um parametro de query)"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_countries_usecase = RegisterCountrySpy(countries_repo, data_covid_consumer)
    register_countries_route = RegisterCountryController(register_countries_usecase)

    attibutes = {"name": faker.random_number(digits=2)}

    response = register_countries_route.route(http_request=HttpRequest(body=attibutes))

    assert register_countries_usecase.name_params["name"] == attibutes["name"]

    assert response.status_code == 422
    assert "error" in response.body


def test_route_fail_400():
    """Testando o erro 422 no método route (com parâmtros errados)"""

    countries_repo = CountryRepoSpy()
    data_covid_consumer = DataCovidConsumerSpy()
    register_countries_usecase = RegisterCountrySpy(countries_repo, data_covid_consumer)
    register_countries_route = RegisterCountryController(register_countries_usecase)

    response = register_countries_route.route(http_request=HttpRequest())

    assert register_countries_usecase.name_params == {}

    assert response.status_code == 400
    assert "error" in response.body
