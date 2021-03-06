"""Classe Spy para GetCountry"""
from typing import Dict, List
from src.domain.models import Country
from src.domain.tests import mock_countries


class GetCountrySpy:
    """Classe para definir o caso de uso: GetCountry"""

    def __init__(self, countries_repo: any) -> None:
        self.countries_repo = countries_repo
        self.by_name_params = {}
        self.by_id_params = {}
        self.all_countries_params = {}

    def by_name(self, name: str) -> Dict[bool, List[Country]]:
        """
        Realiza a busca do país pelo nome.
        :param name: Abreviação do nome do país.
        :return: Um dicionário com as informações do processo.
        """
        self.by_name_params["name"] = name
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_countries()[0]]

        return {"success": validate_entry, "data": response}

    def by_id(self, country_id: int) -> Dict[bool, List[Country]]:
        """
        Realiza a busca do país pelo id.
        :param country_id: id do país cadastrado no banco de dados.
        :return: Um dicionário com as informações do processo.
        """
        self.by_id_params["country_id"] = country_id
        response = None
        validate_entry = isinstance(country_id, int)

        if validate_entry:
            response = [mock_countries()[0]]

        return {"success": validate_entry, "data": response}

    def all_countries(self) -> Dict[bool, List[Country]]:
        """
        Realiza a busca de todos os países cadastrados.
        :return: Um dicionário com as informações do processo.
        """

        self.all_countries_params = {}
        response = mock_countries()

        if response is not None:
            validate_entry = True

        return {"success": validate_entry, "data": response}
