"""Testes relacionados a dominios e casos de uso"""
from src.data.usecases.data_covid_list_colector import DataCovidListColector
from src.infra import DataCovidConsumer
from src import config

def test_list():
    """
    Testando o coletor da lista de dados covid no mundo.
    """
    api_consumer = DataCovidConsumer(config.SEARCH_URL)
    data_covid_list_colector = DataCovidListColector(api_consumer)

    data_covid_list_colector.list()
