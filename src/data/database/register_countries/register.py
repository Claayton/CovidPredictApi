"""Diretório do caso de uso RegisterCountry"""
from typing import Type, Dict, List
from xmlrpc.client import Boolean
from src.domain.models import Country
from src.domain.usecases import (
    RegisterCountriesInterface,
    GetCountriesInterface as GetCountry,
)
from src.data.interfaces import (
    CountryRepoInterface as CountryRepo,
    DataCovidConsumerInterface as DataCovidConsumer,
)


class RegisterCountries(RegisterCountriesInterface):
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
