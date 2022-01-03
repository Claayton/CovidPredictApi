"""Diretório de inicialização e instâncias das classes"""
from src.infra.consumer.data_covid_consumer import DataCovidConsumer
from src.data.colector.data_covid_list_colector import DataCovidListColector
from src.presenters.controllers.consumer.data_covid_list_colector_controller import (
    DataCovidListColectorController,
)
from src import config


def get_data_covid_from_country_composer():
    """Composer"""

    infra = DataCovidConsumer(config.SEARCH_URL)
    usecase = DataCovidListColector(infra)
    controller = DataCovidListColectorController(usecase)

    return controller
