"""Diretório de composer para o caso de uso GetCovidCases"""
from src.data.database.get_covid_cases import GetCovidCases
from src.data.database.get_countries import GetCountry
from src.infra.database.repo import CountryRepo
from src.infra.database.repo import CovidCasesRepo
from src.presenters.controllers.database import GetCovidCasesController


def get_covid_cases_composer():
    """Composer para get_covid_cases_route"""

    countries_repo = CountryRepo()
    get_countries = GetCountry(countries_repo)

    infra = CovidCasesRepo()
    usecase = GetCovidCases(infra)
    controller = GetCovidCasesController(usecase, get_countries)

    return controller
