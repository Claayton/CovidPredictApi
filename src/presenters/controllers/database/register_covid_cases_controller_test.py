"""Testes para a classe RegisterCovidCasesController"""
from faker import Faker
from src.data.tests import RegisterCovidCasesSpy
from . import RegisterCovidCasesController

faker = Faker()


def test_handler():
    """Testando o método handler"""

    register_covid_cases_usecase = RegisterCovidCasesSpy()
    register_covid_cases_controller = RegisterCovidCasesController(
        register_covid_cases_usecase
    )

    response = register_covid_cases_controller.handler(None)

    assert response.status_code == 200
    assert "error" not in response.body
