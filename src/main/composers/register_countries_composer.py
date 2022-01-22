"""Diretório de composer para o caso de uso RegisterCountries"""
from src.infra.database.repo import CountryRepo
from src.data.database.register_countries import RegisterCountry
from src.data.database.get_countries import GetCountry
from src.infra.consumer import DataCovidConsumer
from src.presenters.controllers.database import RegisterCountriesController
from src.config import SEARCH_URL


def register_countries_composer():
    """Composer"""

    countries_repo = CountryRepo()
    get_countries = GetCountry(countries_repo)

    infra_consumer = DataCovidConsumer(SEARCH_URL)
    usecase = RegisterCountry(countries_repo, infra_consumer, get_countries)
    controller = RegisterCountriesController(usecase)

    return controller