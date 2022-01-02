"""Spy para a classe RegisterCountry"""
from typing import Type, Dict
from src.domain.models import Country
from src.domain.usecases import RegisterCountryInterface
from src.data.interfaces import CountryRepoInterface as CountryRepo
from src.domain.tests import mock_countries


class RegisterCountrySpy(RegisterCountryInterface):
    """Classe para definir o Spy para o caso de uso: RegisterCountry"""

    def __init__(self, countries_repo: Type[CountryRepo]) -> None:
        self.countries_repo = countries_repo
        self.name_params = {}

    def register(self, name: str) -> Dict[bool, Country]:
        """
        Registro de países no banco de dados.
        :param name: Abreviação do nome do país cadastrado.
        :return: Um dicionário com as informações do processo.
        """

        self.name_params["name"] = name

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = mock_countries()

        return {"success": validate_entry, "data": response}
