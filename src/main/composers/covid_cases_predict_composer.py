"""Diretório de composer para o caso de uso CovidCasesPredict"""
from typing import Type
from src.data.colector import CovidCasesPredict
from src.data.interfaces import CovidCasesRepoInterface
from src.infra.database.repo import CovidCasesRepo
from src.data.database.get_covid_cases import GetCovidCases
from src.presenters.controllers.colector import CovidCasesPredictController


def covid_cases_predict_composer(
    infra: Type[CovidCasesRepoInterface] = CovidCasesRepo(),
):
    """Composer"""

    get_covid_cases = GetCovidCases(infra)

    usecase = CovidCasesPredict(get_covid_cases)
    controller = CovidCasesPredictController(usecase)

    return controller
