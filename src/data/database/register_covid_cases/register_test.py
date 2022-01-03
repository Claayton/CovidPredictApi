"""Testes para a classe RegisterCovidCases"""
from faker import Faker
from src.infra.tests import CovidCasesRepoSpy, CountryRepoSpy
from src.data.tests import GetCountrySpy
from .register import RegisterCovidCases

faker = Faker()


def test_register():
    """Testando o método register"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_countries = GetCountrySpy(CountryRepoSpy())
    register_covid_cases = RegisterCovidCases(covid_cases_repo, get_countries)

    attributes = {
        "date": faker.date(),
        "new_cases": faker.random_number(digits=4),
        "country": faker.name(),
    }

    response = register_covid_cases.register(
        date=attributes["date"],
        new_cases=attributes["new_cases"],
        country=attributes["country"],
    )

    assert covid_cases_repo.insert_data_params["data_date"] == attributes["date"]
    assert covid_cases_repo.insert_data_params["new_cases"] == attributes["new_cases"]

    assert get_countries.by_name_params["name"] == attributes["country"]

    assert response["success"] is True
    assert response["data"]


def test_register_fail():
    """Testando o erro no método register"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_countries = GetCountrySpy(CountryRepoSpy())
    register_covid_cases = RegisterCovidCases(covid_cases_repo, get_countries)

    attributes = {
        "date": faker.date(),
        "new_cases": faker.random_number(digits=4),
        "country": faker.name(),
    }

    response = register_covid_cases.register(
        date=attributes["date"],
        new_cases=attributes["new_cases"],
        country=attributes["country"],
    )

    assert covid_cases_repo.insert_data_params["data_date"] == attributes["date"]
    assert covid_cases_repo.insert_data_params["new_cases"] == attributes["new_cases"]

    assert get_countries.by_name_params["name"] == attributes["country"]

    assert response["success"] is True
    assert response["data"]
