"""Diretório de composer para o caso de uso GetCountry"""
from src.infra.database.repo import CountryRepo
from src.data.database.get_countries import GetCountry
from src.presenters.controllers.database.get_countries_controller import (
    GetCountryController,
)


def get_countries_composer():
    """Composer"""

    repository = CountryRepo()
    usecase = GetCountry(repository)
    controller = GetCountryController(usecase)

    return controller
