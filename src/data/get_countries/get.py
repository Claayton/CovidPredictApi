"""Caso de uso GetCountries"""
from typing import List, Type, Dict
from src.domain.usecases import GetCountriesInterface
from src.data.interfaces import CountryRepoInterface as CountryRepo
from src.domain.models import Country


class GetCountry(GetCountriesInterface):
    """Classe para definir o caso de uso Get Country"""

    def __init__(self, countries_repo: Type[CountryRepo]) -> None:
        self.countries_repo = countries_repo

    def by_name(self, name: str) -> Dict[bool, List[Country]]:
        """
        Realiza a busca do país pelo nome.
        :param name: Abreviação do nome do país.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.countries_repo.get_countries(name=name)

        return {"success": validate_entry, "data": response}

    def all_countries(self) -> Dict[bool, List[Country]]:
        """
        Realiza a busca de todos os países cadastrados.
        :return: Um dicionário com as informações do processo.
        """

        response = self.countries_repo.get_countries()
        if response is not None:
            validate_entry = True

        return {"success": validate_entry, "data": response}
