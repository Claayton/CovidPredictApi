"""Testes para a classe CovidCasesColector"""
from src.infra.tests.data_covid_consumer_spy import DataCovidConsumerSpy
from src.data.colector import CovidCasesColector
from src.data.tests import GetCountrySpy


def test_covid_cases_country():
    """Testando o método covid_cases_country"""

    api_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    attribute = {"country": "BRA"}

    response = covid_cases_colector.covid_cases_country(attribute["country"])

    api_consumer_attributes = api_consumer.get_data_covid_by_country_attributes[
        "country"
    ]

    # Teste de entrada:
    # Testando se os atributos enviados para a api_consumer são os mesmos enviados para o método.
    assert api_consumer_attributes == attribute["country"]

    # Teste de saída:
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)
    assert isinstance(response["data"][0], dict)
    assert "new_cases" in response["data"][0]
    assert "date" in response["data"][0]


def test_covid_cases_country_error():
    """
    Testando o erro no método covid_cases_country.
    Enviando um número inteiro para o atributo country que deveria ser uma string.
    """

    api_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    attributes = {"country": 5}

    response = covid_cases_colector.covid_cases_country(attributes["country"])

    api_consumer_attributes = api_consumer.get_data_covid_by_country_attributes

    # Teste de entrada:
    # Testando se os atributos enviados para a api_consumer são os mesmos enviados para o método.
    assert api_consumer_attributes == {}

    # Testando a saída
    assert response["success"] is False
    assert "error" in response["data"]
