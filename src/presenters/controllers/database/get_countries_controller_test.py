"""Testes para a classe GetCountryController"""
from faker import Faker
from src.data.tests import GetCountrySpy
from src.infra.tests import CountryRepoSpy
from src.presenters.helpers import HttpRequest
from .get_countries_controller import GetCountryController

faker = Faker()


def test_handler():
    """Testando o método handler"""

    get_countries_usecase = GetCountrySpy(CountryRepoSpy())
    get_countries_controller = GetCountryController(get_countries_usecase)
    http_request = HttpRequest(query={"name": faker.name()})

    response = get_countries_controller.handler(http_request)

    assert get_countries_usecase.by_name_params["name"] == http_request.query["name"]

    assert response.status_code == 200
    assert response.body


def test_handler_fail_422():
    """Testando o erro 422 no método handler (com parâmtros errados)"""

    get_countries_usecase = GetCountrySpy(CountryRepoSpy())
    get_countries_controller = GetCountryController(get_countries_usecase)
    http_request = HttpRequest(query={"name": faker.random_number(digits=2)})

    response = get_countries_controller.handler(http_request)

    assert get_countries_usecase.by_name_params["name"] == http_request.query["name"]

    assert response.status_code == 422
    assert "error" in response.body
