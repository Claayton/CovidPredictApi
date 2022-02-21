"""Testes para a classe CovidCasesColector"""
from src.infra.tests.data_covid_consumer_spy import DataCovidConsumerSpy
from src.data.colector import CovidCasesColector
from src.data.tests import GetCountrySpy


def test_covid_cases_colector_without_country_param():
    """Testando o método covid_cases_colector sem utilizar o parametro 'country'"""

    api_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    response = covid_cases_colector.covid_cases_colector()

    # Teste de entrada:
    # Testando se os atributos enviados para a api_consumer são os mesmos enviados para o método.
    assert api_consumer.get_data_covid_by_country_attributes == {}

    # Teste de saída:
    assert isinstance(response, dict)
    assert isinstance(response["data"], dict)
    assert isinstance(response["data"]["BRA"], list)
    assert "new_cases" in response["data"]["BRA"][0]
    assert "date" in response["data"]["BRA"][0]


def test_covid_cases_colector_with_country_param():
    """Testando o método covid_cases_colector com um valor valido para o parametro 'country'"""

    api_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    attribute = {"country": "BRA"}

    response = covid_cases_colector.covid_cases_colector(attribute["country"])

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


def test_covid_cases_colector_with_country_param_error():
    """
    Testando o erro no método covid_cases_colector.
    Enviando um número inteiro para o parametro 'country' que deveria ser uma string.
    """

    api_consumer = DataCovidConsumerSpy()
    get_countries = GetCountrySpy(None)
    covid_cases_colector = CovidCasesColector(api_consumer, get_countries)

    attributes = {"country": 5}

    response = covid_cases_colector.covid_cases_colector(attributes["country"])

    api_consumer_attributes = api_consumer.get_data_covid_by_country_attributes

    # Teste de entrada:
    # Testando se os atributos enviados para a api_consumer é igual a {},
    # pois os attributos enviado são inválidos.
    assert api_consumer_attributes == {}

    # Testando a saída:
    assert response["success"] is False
    assert "error" in response["data"]
