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


def test_handler_fail():
    """Testando o erro no método handler (sem um parametro de query)"""

    get_countries_usecase = GetCountrySpy(CountryRepoSpy())
    get_countries_controller = GetCountryController(get_countries_usecase)
    http_request = HttpRequest()

    response = get_countries_controller.handler(http_request)

    assert get_countries_usecase.by_name_params == {}

    assert response.status_code == 400
    assert "error" in response.body
