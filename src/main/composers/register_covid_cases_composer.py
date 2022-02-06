"""Diretório de composer para o caso de uso RegisterCovidCases"""
from typing import Type
from src.data.interfaces import CountryRepoInterface, DataCovidConsumerInterface
from src.data.colector import CovidCasesColector
from src.data.interfaces.covid_cases_repo_interface import CovidCasesRepoInterface
from src.infra.consumer import DataCovidConsumer
from src.infra.database.repo import CountryRepo, CovidCasesRepo
from src.data.database.register_covid_cases import RegisterCovidCases
from src.data.database.get_countries import GetCountry
from src.presenters.controllers.database import RegisterCovidCasesController
from src.config import SEARCH_URL


def register_covid_cases_composer(
    infra_repository_countries: Type[CountryRepoInterface] = CountryRepo(),
    infra_repository_covid_cases: Type[CovidCasesRepoInterface] = CovidCasesRepo(),
    infra_consumer: Type[DataCovidConsumerInterface] = DataCovidConsumer(SEARCH_URL),
):
    """Composer"""

    get_countries = GetCountry(infra_repository_countries)
    covid_cases_colector = CovidCasesColector(infra_consumer, get_countries)

    usecase = RegisterCovidCases(
        covid_cases_colector, infra_repository_covid_cases, get_countries
    )

    controller = RegisterCovidCasesController(usecase)

    return controller
