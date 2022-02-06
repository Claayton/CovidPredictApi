"""Diretório de composer para o caso de uso CovidCasesColector"""
from typing import Type
from src.data.interfaces.countries_repo_interface import CountryRepoInterface
from src.data.interfaces.data_covid_consumer import DataCovidConsumerInterface
from src.infra.consumer import DataCovidConsumer
from src.infra.database.repo import CountryRepo
from src.data.colector import CovidCasesColector
from src.data.database.get_countries import GetCountry
from src.presenters.controllers.colector import CovidCasesColectorController
from src.config import SEARCH_URL


def covid_cases_colector_composer(
    infra: Type[DataCovidConsumerInterface] = DataCovidConsumer(SEARCH_URL),
    countries_repo: Type[CountryRepoInterface] = CountryRepo(),
):
    """Composer"""

    get_countries = GetCountry(countries_repo)

    usecase = CovidCasesColector(infra, get_countries)
    controller = CovidCasesColectorController(usecase)

    return controller
