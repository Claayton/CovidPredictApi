"""Diretório do caso de uso RegisterCountry"""
from typing import Type, Dict
from src.domain.models import Country
from src.domain.usecases import RegisterCountryInterface
from src.data.interfaces import CountryRepoInterface as CountryRepo


class RegisterCountry(RegisterCountryInterface):
    """Classe para definir o caso de uso: RegisterCountry"""

    def __init__(self, countries_repo: Type[CountryRepo]) -> None:
        self.countries_repo = countries_repo

    def register(self, name: str) -> Dict[bool, Country]:
        """
        Registro de países no banco de dados.
        :param name: Abreviação do nome do país cadastrado.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.countries_repo.insert_country(name)

        return {"sucess": validate_entry, "data": response}
