"""Diretório do caso de uso RegisterCountry"""
from typing import Type, Dict, List
from xmlrpc.client import Boolean
from src.domain.models import Country
from src.errors import HttpUnprocessableEntityError, HttpBadRequestError
from src.domain.usecases import (
    RegisterCountryInterface,
    GetCountriesInterface as GetCountry,
)
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
        get_countries: Type[GetCountry],
    ) -> None:
        self.__countries_repo = countries_repo
        self.__data_covid_consumer = data_covid_consumer
        self.__get_countries = get_countries

    def register_country(self, name: str) -> Dict[bool, Country]:
        """
        Registro de um país no banco de dados.
        :param name: Abreviação do nome do país em maiúsculo para o cadastro.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(name, str) and name.isupper()

        if self.__registered_country(country_name=name):
            raise HttpBadRequestError(message="country already registered")

        if not validate_entry:
            raise HttpUnprocessableEntityError(
                message="'name' must be string and capitalized"
            )

        response = self.__countries_repo.insert_country(name)

        return {"success": validate_entry, "data": response}

    def register_countries(self) -> Dict[bool, List[Country]]:
        """
        Registro de países no banco de dados.
        :return: Um dicionário com as informações do processo.
        """

        countries = self.__data_covid_consumer.get_countries().response
        response = []
        validate_entry = isinstance(countries, list)

        if validate_entry:
            for country in countries:

                if self.__registered_country(country_name=country):
                    continue

                insersion = self.__countries_repo.insert_country(country)
                response.append(insersion)

        return {"success": validate_entry, "data": response}

    def __registered_country(self, country_name: str) -> Boolean:

        countries = self.__get_countries.all_countries()

        for country in countries["data"]:

            if country_name == str(country.name):

                return True
        return False
