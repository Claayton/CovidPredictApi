"""Diretório de composer para o caso de uso CovidCasesColector"""
from src.infra.consumer import DataCovidConsumer
from src.infra.database.repo import CountryRepo
from src.data.colector import CovidCasesColector
from src.data.database.get_countries import GetCountry
from src.presenters.controllers.colector import CovidCasesColectorController
from src.config import SEARCH_URL


def covid_cases_colector_composer():
    """Composer"""

    countries_repo = CountryRepo()
    get_countries = GetCountry(countries_repo)

    infra = DataCovidConsumer(SEARCH_URL)
    usecase = CovidCasesColector(infra, get_countries)
    controller = CovidCasesColectorController(usecase)

    return controller
