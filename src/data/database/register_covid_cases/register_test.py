"""Testes para a classe RegisterCovidCases"""
from faker import Faker
from src.infra.tests import CovidCasesRepoSpy, CountryRepoSpy, DataCovidConsumerSpy
from src.data.tests import GetCountrySpy
from src.data.colector import CovidCasesColector
from .register import RegisterCovidCases

faker = Faker()


def test_register_covid_cases_by_country():
    """Testando o método register_covid_cases_by_country"""

    covid_cases_repo = CovidCasesRepoSpy()
    countries_repo = CountryRepoSpy()
    get_countries = GetCountrySpy(countries_repo)
    api_consumer = DataCovidConsumerSpy()
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)
    register_covid_cases = RegisterCovidCases(covid_cases_colector, covid_cases_repo, get_countries)

    attributes = {"country": "BRA"}

    response = register_covid_cases.register_covid_cases_by_country(country=attributes["country"])

    assert get_countries.by_name_params["name"] == attributes["country"]

    assert response["success"] is True
    assert response["data"]


def test_register_covid_cases_by_country_fail():
    """Testando o erro no método register_covid_cases_by_country"""

    covid_cases_repo = CovidCasesRepoSpy()
    countries_repo = CountryRepoSpy()
    get_countries = GetCountrySpy(countries_repo)
    api_consumer = DataCovidConsumerSpy()
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)
    register_covid_cases = RegisterCovidCases(covid_cases_colector, covid_cases_repo, get_countries)

    attributes = {"country": 123}

    response = register_covid_cases.register_covid_cases_by_country(country=attributes["country"])

    assert get_countries.by_name_params == {}

    assert response["success"] is False
    assert response["data"] == []
