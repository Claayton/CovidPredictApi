"""Testes para a classe RegisterCovidCaseController"""
from faker import Faker
from src.data.tests import RegisterCovidCasesSpy
from src.infra.tests import CovidCasesRepoSpy
from src.presenters.helpers import HttpRequest
from . import RegisterCovidCaseController

faker = Faker()


def test_route():
    """Testando o método route"""

    register_covid_cases_usecase = RegisterCovidCasesSpy(CovidCasesRepoSpy(), None)
    register_covid_cases_route = RegisterCovidCaseController(
        register_covid_cases_usecase
    )

    attibutes = {
        "date": faker.date(),
        "new_cases": faker.random_number(digits=3),
        "country": faker.name(),
    }

    response = register_covid_cases_route.handler(
        http_request=HttpRequest(body=attibutes)
    )

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
