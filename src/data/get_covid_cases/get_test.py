"""Diretório de tests para a classe GetCovidCases"""
from faker import Faker
from src.infra.tests import CovidCasesRepoSpy
from .get import GetCovidCases

faker = Faker()


def test_by_country():
    """Testando o método by_country"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attributes = {"country": faker.name()}
    response = get_covid_cases.by_country(country=attributes["country"])

    assert covid_cases_repo.get_covid_cases_params["country"] == attributes["country"]

    assert response["success"] is True
    assert response["data"]


def test_by_date():
    """Testando o método by_date"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attributes = {"data_date": faker.date()}
    response = get_covid_cases.by_date(data_date=attributes["data_date"])

    assert (
        covid_cases_repo.get_covid_cases_params["data_date"] == attributes["data_date"]
    )

    assert response["success"] is True
    assert response["data"]


def test_by_country_and_by_date():
    """Testando o erro no método by_country_and_by_date"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attributes = {"country": faker.name(), "data_date": faker.date()}
    response = get_covid_cases.by_country_and_by_date(
        country=attributes["country"], data_date=attributes["data_date"]
    )

    assert covid_cases_repo.get_covid_cases_params["country"] == attributes["country"]
    assert (
        covid_cases_repo.get_covid_cases_params["data_date"] == attributes["data_date"]
    )

    assert response["success"] is True
    assert response["data"]
