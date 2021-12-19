"""Testes relacionados a dominios e casos de uso"""
from src.data.usecases.data_covid_list_colector import DataCovidListColector
from src.infra.tests.data_covid_consumer import DataCovidConsumerSpy


def test_list():
    """
    Testando o coletor da lista de dados covid no mundo.
    """
    api_consumer = DataCovidConsumerSpy()
    data_covid_list_colector = DataCovidListColector(api_consumer)

    country = ["BRA"]
    response = data_covid_list_colector.list()

    assert api_consumer.get_data_covid_attributes == {"country": country}
    assert isinstance(response, list)
    assert "country" in response[0]
    assert "new_cases" in response[0]["data"][0]
