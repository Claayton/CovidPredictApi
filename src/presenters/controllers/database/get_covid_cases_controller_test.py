"""Testes para a classe GetCovidCasescontroller"""
from faker import Faker
from src.data.tests import GetCovidCasesSpy
from src.infra.tests import CovidCasesRepoSpy
from src.presenters.helpers import HttpRequest
from .get_covid_cases_controller import GetCovidCasesController

faker = Faker()


def test_handler():
    """Testando o método handler"""

    get_covid_cases_usecase = GetCovidCasesSpy(CovidCasesRepoSpy())
    get_covid_cases_controller = GetCovidCasesController(get_covid_cases_usecase)
    http_request = HttpRequest(
        query={
            "date": faker.date(),
            "new_cases": faker.random_number(digits=3),
            "country": faker.name(),
        }
    )

    response = get_covid_cases_controller.handler(http_request)

    assert (
        get_covid_cases_usecase.by_country_and_by_date_params["date"]
        == http_request.query["date"]
    )
    assert (
        get_covid_cases_usecase.by_country_and_by_date_params["country"]
        == http_request.query["country"]
    )

    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_by_country():
    """Testando o método handler"""

    get_covid_cases_usecase = GetCovidCasesSpy(CovidCasesRepoSpy())
    get_covid_cases_controller = GetCovidCasesController(get_covid_cases_usecase)
    http_request = HttpRequest(query={"country": faker.name()})

    response = get_covid_cases_controller.handler(http_request)

    assert (
        get_covid_cases_usecase.by_country_params["country"]
        == http_request.query["country"]
    )

    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_by_date():
    """Testando o método handler"""

    get_covid_cases_usecase = GetCovidCasesSpy(CovidCasesRepoSpy())
    get_covid_cases_controller = GetCovidCasesController(get_covid_cases_usecase)
    http_request = HttpRequest(query={"date": faker.date()})

    response = get_covid_cases_controller.handler(http_request)

    assert get_covid_cases_usecase.by_date_params["date"] == http_request.query["date"]

    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_fail_422():
    """Testando o erro 422 no método handler (com parâmtros errados)"""

    get_covid_cases_usecase = GetCovidCasesSpy(CovidCasesRepoSpy())
    get_covid_cases_controller = GetCovidCasesController(get_covid_cases_usecase)
    http_request = HttpRequest(
        query={
            "date": faker.random_number(digits=3),
            "new_cases": faker.name(),
            "country": faker.random_number(digits=3),
        }
    )

    response = get_covid_cases_controller.handler(http_request)

    assert (
        get_covid_cases_usecase.by_country_and_by_date_params["date"]
        == http_request.query["date"]
    )
    assert (
        get_covid_cases_usecase.by_country_and_by_date_params["country"]
        == http_request.query["country"]
    )

    assert response.status_code == 422
    assert "error" in response.body
