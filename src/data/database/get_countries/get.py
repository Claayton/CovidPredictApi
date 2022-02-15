"""Caso de uso GetCountries"""
from typing import List, Type, Dict
from src.domain.usecases import GetCountriesInterface
from src.data.interfaces import CountryRepoInterface as CountryRepo
from src.domain.models import Country


class GetCountry(GetCountriesInterface):
    """Classe para definir o caso de uso Get Country"""

    def __init__(self, countries_repo: Type[CountryRepo]) -> None:
        self.__countries_repo = countries_repo

    def by_name(self, name: str) -> Dict[bool, List[Country]]:
        """
        Realiza a busca do país pelo nome.
        :param name: Abreviação do nome do país.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.__countries_repo.get_countries(name=name)

        return {"success": validate_entry, "data": response}

    def by_id(self, country_id: int) -> Dict[bool, List[Country]]:
        """
        Realiza a busca do país pelo id.
        :param country_id: id do país cadastrado no banco de dados.
        :return: Um dicionário com as informações do processo.
        """
        response = None
        validate_entry = isinstance(country_id, int)

        if validate_entry:
            response = self.__countries_repo.get_countries(country_id=country_id)

        return {"success": validate_entry, "data": response}

    def all_countries(self) -> Dict[bool, List[Country]]:
        """
        Realiza a busca de todos os países cadastrados.
        :return: Um dicionário com as informações do processo.
        """
        validate_entry = True

        response = self.__countries_repo.get_countries()

        if response is None:

            validate_entry = False

        return {"success": validate_entry, "data": response}
