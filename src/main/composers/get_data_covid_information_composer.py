"""Diretório de inicialização e instâncias das classes"""
from src.infra.consumer.data_covid_consumer import DataCovidConsumer
from src.data.usecases.data_covid_information_colector import (
    DataCovidInformationColector,
)
from src.presenters.controllers.consumer.data_covid_information_colector_controller import (
    DataCovidInformationColectorController,
)
from src import config


def get_data_covid_information_composer():
    """Composer"""

    infra = DataCovidConsumer(config.SEARCH_URL)
    usecase = DataCovidInformationColector(infra)
    controller = DataCovidInformationColectorController(usecase)

    return controller
