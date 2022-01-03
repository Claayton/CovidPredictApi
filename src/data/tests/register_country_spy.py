"""Spy para a classe RegisterCountry"""
from typing import Type, Dict, List
from src.domain.models import Country
from src.domain.usecases import RegisterCountryInterface
from src.domain.tests import mock_countries
from src.data.interfaces import (
    CountryRepoInterface as CountryRepo,
    DataCovidConsumerInterface as DataCovidConsumer,
)


class RegisterCountrySpy(RegisterCountryInterface):
    """Classe para definir o Spy para o caso de uso: RegisterCountry"""

    def __init__(
        self,
        countries_repo: Type[CountryRepo],
        data_covid_consumer: Type[DataCovidConsumer],
    ) -> None:
        self.name_params = {}
        self.countries_repo = countries_repo
        self.data_covid_consumer = data_covid_consumer

    def register_country(self, name: str) -> Dict[bool, Country]:
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

    def register_countries(self) -> Dict[bool, List[Country]]:
        """
        Registro de países no banco de dados.
        :return: Um dicionário com as informações do processo.
        """

        countries = self.data_covid_consumer.get_countries().response
        response = []
        validate_entry = isinstance(countries, list)

        if validate_entry:
            for country in countries:
                insersion = mock_countries()
                response.append(insersion)

        return {"success": validate_entry, "data": response}
