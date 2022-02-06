"""Spy para a classe RegisterCountry"""
from typing import Type, Dict, List
from src.domain.models import Country
from src.domain.usecases import RegisterCountriesInterface
from src.domain.tests import mock_countries
from src.data.interfaces import (
    CountryRepoInterface as CountryRepo,
    DataCovidConsumerInterface as DataCovidConsumer,
)


class RegisterCountriesSpy(RegisterCountriesInterface):
    """Classe para definir o Spy para o caso de uso: RegisterCountry"""

    def __init__(
        self,
        countries_repo: Type[CountryRepo],
        data_covid_consumer: Type[DataCovidConsumer],
    ) -> None:
        self.name_params = {}
        self.countries_repo = countries_repo
        self.data_covid_consumer = data_covid_consumer

    def register_countries(self) -> Dict[bool, List[Country]]:
        """
        Registro de países no banco de dados.
        :return: Um dicionário com as informações do processo.
        """

        countries = self.data_covid_consumer.get_countries().response
        response = []
        validate_entry = isinstance(countries, list)

        if validate_entry:
            for country in countries:  # pylint: disable=unused-variable

                insersion = mock_countries()
                response.append(insersion)

        return {"success": validate_entry, "data": response}
