"""Testes para a classe RegisterCovidCases"""
from faker import Faker
from src.infra.tests import CovidCasesRepoSpy, DataCovidConsumerSpy
from src.data.tests import GetCountrySpy
from src.data.colector import CovidCasesColector
from . import RegisterCovidCases

faker = Faker()


def test_register_covid_cases():
    """Testando o método register_all_covid_cases"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_countries = GetCountrySpy(None)
    api_consumer = DataCovidConsumerSpy()
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)
    register_covid_cases = RegisterCovidCases(
        covid_cases_colector, covid_cases_repo, get_countries
    )

    response = register_covid_cases.register_covid_cases()

    assert response["success"] is True
    assert response["data"] is not None
    assert "error" not in response
