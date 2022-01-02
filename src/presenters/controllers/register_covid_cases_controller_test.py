"""Testes para a classe RegisterCovidCasesController"""
from faker import Faker
from src.data.tests import RegisterCovidCasesSpy
from src.infra.tests import CovidCasesRepoSpy
from src.presenters.helpers import HttpRequest
from . import RegisterCoviCasesController

faker = Faker()


def test_route():
    """Testando o método route"""

    register_covid_cases_usecase = RegisterCovidCasesSpy(CovidCasesRepoSpy(), None)
    register_covid_cases_route = RegisterCoviCasesController(
        register_covid_cases_usecase
    )

    attibutes = {
        "date": faker.date(),
        "new_cases": faker.random_number(digits=3),
        "country": faker.name(),
    }

    response = register_covid_cases_route.route(
        http_request=HttpRequest(body=attibutes)
    )
    print(response)

    assert register_covid_cases_usecase.register_params["date"] == attibutes["date"]
    assert (
        register_covid_cases_usecase.register_params["new_cases"]
        == attibutes["new_cases"]
    )
    assert (
        register_covid_cases_usecase.register_params["country"] == attibutes["country"]
    )

    assert response.status_code == 200
    assert "error" not in response.body


def test_route_fail_422():
    """Testando o erro 400 no método route (sem um parametro de query)"""

    register_covid_cases_usecase = RegisterCovidCasesSpy(CovidCasesRepoSpy(), None)
    register_covid_cases_route = RegisterCoviCasesController(
        register_covid_cases_usecase
    )

    attibutes = {
        "date": faker.random_number(digits=3),
        "new_cases": faker.date(),
        "country": faker.random_number(digits=3),
    }

    response = register_covid_cases_route.route(
        http_request=HttpRequest(body=attibutes)
    )
    print(response)

    assert register_covid_cases_usecase.register_params["date"] == attibutes["date"]
    assert (
        register_covid_cases_usecase.register_params["new_cases"]
        == attibutes["new_cases"]
    )
    assert (
        register_covid_cases_usecase.register_params["country"] == attibutes["country"]
    )

    assert response.status_code == 422
    assert "error" in response.body


def test_route_fail_400():
    """Testando o erro 422 no método route (com parâmtros errados)"""

    register_covid_cases_usecase = RegisterCovidCasesSpy(CovidCasesRepoSpy(), None)
    register_covid_cases_route = RegisterCoviCasesController(
        register_covid_cases_usecase
    )

    response = register_covid_cases_route.route(http_request=HttpRequest())
    print(response)

    assert register_covid_cases_usecase.register_params == {}

    assert response.status_code == 400
    assert "error" in response.body
