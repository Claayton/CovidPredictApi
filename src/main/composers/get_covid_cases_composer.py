"""Diretório de composer para o caso de uso GetCovidCases"""
from typing import Type
from src.data.database.get_covid_cases import GetCovidCases
from src.data.database.get_countries import GetCountry
from src.data.interfaces import CountryRepoInterface, CovidCasesRepoInterface
from src.infra.database.repo import CountryRepo
from src.infra.database.repo import CovidCasesRepo
from src.presenters.controllers.database import GetCovidCasesController


def get_covid_cases_composer(
    countries_repo: Type[CountryRepoInterface] = CountryRepo(),
    infra: Type[CovidCasesRepoInterface] = CovidCasesRepo(),
):
    """Composer para get_covid_cases_route"""

    get_countries = GetCountry(countries_repo)

    usecase = GetCovidCases(infra)
    controller = GetCovidCasesController(usecase, get_countries)

    return controller
