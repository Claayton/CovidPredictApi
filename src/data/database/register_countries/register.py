"""Diretório do caso de uso RegisterCountry"""
from typing import Type, Dict, List
from src.domain.models import Country
from src.domain.usecases import RegisterCountryInterface
from src.data.interfaces import (
    CountryRepoInterface as CountryRepo,
    DataCovidConsumerInterface as DataCovidConsumer,
)


class RegisterCountry(RegisterCountryInterface):
    """Classe para definir o caso de uso: RegisterCountry"""

    def __init__(
        self,
        countries_repo: Type[CountryRepo],
        data_covid_consumer: Type[DataCovidConsumer],
    ) -> None:
        self.countries_repo = countries_repo
        self.data_covid_consumer = data_covid_consumer

    def register_country(self, name: str) -> Dict[bool, Country]:
        """
        Registro de um país no banco de dados.
        :param name: Abreviação do nome do país em maiúsculo para o cadastro.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(name, str) and name.isupper()

        if validate_entry:
            response = self.countries_repo.insert_country(name)

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
                insersion = self.countries_repo.insert_country(country)
                response.append(insersion)

        return {"success": validate_entry, "data": response}
