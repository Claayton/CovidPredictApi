"""Testes para a classe CovidCasesColectorController"""
from faker import Faker
from src.data.tests import CovidCasesColectorSpy
from src.infra.tests import CountryRepoSpy
from src.data.tests import GetCountrySpy
from src.presenters.helpers import HttpRequest
from .covid_cases_colector_controller import CovidCasesColectorController

faker = Faker()


def test_handler_full_query():
    """Testando o método handler"""

    countries_repo = CountryRepoSpy()
    get_countries = GetCountrySpy(countries_repo)
    covid_cases_colector_usecase = CovidCasesColectorSpy(get_countries)
    covid_cases_colector_controller = CovidCasesColectorController(
        covid_cases_colector_usecase
    )

    http_request = HttpRequest(
        query={"country": faker.name(), "days": faker.random_number(digits=1)}
    )

    response = covid_cases_colector_controller.handler(http_request)

    assert (
        covid_cases_colector_usecase.covid_cases_country_attributes["country"]
        == http_request.query["country"]
    )

    assert response.status_code == 200
    assert response.body


def test_handler_with_country_query():
    """Testando o método handler"""

    countries_repo = CountryRepoSpy()
    get_countries = GetCountrySpy(countries_repo)
    covid_cases_colector_usecase = CovidCasesColectorSpy(get_countries)
    covid_cases_colector_controller = CovidCasesColectorController(
        covid_cases_colector_usecase
    )

    http_request = HttpRequest(query={"country": faker.name()})

    response = covid_cases_colector_controller.handler(http_request)

    assert (
        covid_cases_colector_usecase.covid_cases_country_attributes["country"]
        == http_request.query["country"]
    )

    assert response.status_code == 200
    assert response.body
