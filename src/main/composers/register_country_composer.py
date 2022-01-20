"""Diretório de composer para o caso de uso RegisterCountry"""
from src.infra.database.repo import CountryRepo
from src.data.database.register_countries import RegisterCountry
from src.data.database.get_countries import GetCountry
from src.infra.consumer import DataCovidConsumer
from src.presenters.controllers.database import RegisterCountryController
from src.config import SEARCH_URL


def register_country_composer():
    """Composer"""

    countries_repo = CountryRepo()
    get_countries = GetCountry(countries_repo)

    infra_consumer = DataCovidConsumer(SEARCH_URL)
    usecase = RegisterCountry(countries_repo, infra_consumer, get_countries)
    controller = RegisterCountryController(usecase)

    return controller
