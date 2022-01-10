"""Diretório de composer para o caso de uso GetCovidCases"""
from src.data.database.get_covid_cases import GetCovidCases
from src.infra.database.repo import CovidCasesRepo
from src.presenters.controllers.database import GetCovidCasesController


def get_covid_cases_composer():
    """Composer"""

    infra = CovidCasesRepo()
    usecase = GetCovidCases(infra)
    controller = GetCovidCasesController(usecase)

    return controller
