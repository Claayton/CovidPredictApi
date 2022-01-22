"""Diretório de composer para o caso de uso RegisterCountries"""
from typing import Type
from src.data.interfaces import CountryRepoInterface
from src.infra.database.repo import CountryRepo
from src.data.database.register_countries import RegisterCountry
from src.data.database.get_countries import GetCountry
from src.infra.consumer import DataCovidConsumer
from src.presenters.controllers.database import RegisterCountriesController
from src.config import SEARCH_URL


def register_countries_composer(
    infra_repository: Type[CountryRepoInterface] = CountryRepo(),
):
    """Composer"""

    get_countries = GetCountry(infra_repository)

    infra_consumer = DataCovidConsumer(SEARCH_URL)
    usecase = RegisterCountry(infra_repository, infra_consumer, get_countries)
    controller = RegisterCountriesController(usecase)

    return controller
