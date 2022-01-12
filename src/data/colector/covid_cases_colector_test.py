"""Testes para a classe CovidCasesColector"""
from src.data.colector import CovidCasesColector
from src.infra.tests.data_covid_consumer_spy import DataCovidConsumerSpy
from src.data.tests import GetCountrySpy
from src.infra.database.repo import CountryRepo


def test_covid_cases_country():
    """Testando o método covid_cases_country"""

    api_consumer = DataCovidConsumerSpy()
    countries_repo = CountryRepo()
    get_countries = GetCountrySpy(countries_repo)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    country = "BRA"
    days = 4

    response = covid_cases_colector.covid_cases_country(country, days)

    assert api_consumer.get_data_covid_by_country_attributes["country"] == country

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert "new_cases" in response[0]
    assert "date" in response[0]


def test_covid_cases_country_error():
    """Testando o erro no método covid_cases_country"""

    api_consumer = DataCovidConsumerSpy()
    countries_repo = CountryRepo()
    get_countries = GetCountrySpy(countries_repo)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    country = 5
    days = 4

    response = covid_cases_colector.covid_cases_country(country, days)

    assert api_consumer.get_data_covid_by_country_attributes == {}

    assert "error" in response[0]["body"]
    assert "success" not in response[0]["body"]
    assert "data" not in response[0]["body"]


def test_covid_cases_world():
    """Testando o método covid_cases_world"""

    api_consumer = DataCovidConsumerSpy()
    countries_repo = CountryRepo()
    get_countries = GetCountrySpy(countries_repo)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    days = 4

    response = covid_cases_colector.covid_cases_world(days)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert "new_cases" in response[0]
    assert "date" in response[0]
