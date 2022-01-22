"""Diretório de composer para o caso de uso GetCountry"""
from typing import Type
from src.data.interfaces import CountryRepoInterface
from src.infra.database.repo import CountryRepo
from src.data.database.get_countries import GetCountry
from src.presenters.controllers.database import GetCountryController


def get_countries_composer(infra: Type[CountryRepoInterface] = CountryRepo()):
    """Composer"""

    usecase = GetCountry(infra)
    controller = GetCountryController(usecase)

    return controller
