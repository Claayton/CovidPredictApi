"""Diretório de inicialização e instâncias das classes"""
from src.data.database.get_countries import GetCountry
from src.infra.database.repo import CountryRepo
from src.infra.consumer.data_covid_consumer import DataCovidConsumer
from src.data.colector.covid_cases_colector import (
    CovidCasesColector,
)
from src.presenters.controllers.consumer.data_covid_information_colector_controller import (
    DataCovidInformationColectorController,
)
from src import config


def get_data_covid_information_composer():
    """Composer"""

    infra = DataCovidConsumer(config.SEARCH_URL)
    countries_repo = CountryRepo()
    get_countries = GetCountry(countries_repo)
    usecase = CovidCasesColector(infra, get_countries)
    controller = DataCovidInformationColectorController(usecase)

    return controller
