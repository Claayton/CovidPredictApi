"""Casos de uso para GetCovidCases"""
from typing import List, Dict, Type
from src.domain.usecases import GetCovidCasesInterface
from src.data.interfaces import CovidCasesRepoInterface as CovidCasesRepo
from src.domain.models import CovidCases


class GetCovidCases(GetCovidCasesInterface):
    """Classe para definir o caso de uso GetCovidCases"""

    def __init__(self, covid_cases_repo: Type[CovidCasesRepo]) -> None:
        self.__covid_cases_repo = covid_cases_repo

    def by_country(self, country: str) -> Dict[bool, List[CovidCases]]:
        """
        Realiza a busca dos casos de covid19 por país.
        :param country: Abreviação do nome do país.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(country, str)

        if validate_entry:
            response = self.__covid_cases_repo.get_data(country=country)

        return {"success": validate_entry, "data": response}

    def by_date(self, data_date: str) -> Dict[bool, List[CovidCases]]:
        """
        Realiza a busca dos casos de covid19 por data.
        :param data_date: Data para a busca.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(data_date, str)

        if validate_entry:
            response = self.__covid_cases_repo.get_data(data_date=data_date)

        return {"success": validate_entry, "data": response}

    def by_country_and_by_date(
        self, country: str, data_date: str
    ) -> Dict[bool, List[CovidCases]]:
        """
        Realiza a busca dos casos de covid19 tanto por país, quanto pela data.
        :param country: Abreviação do nome do país.
        :param data_date: Data para a busca.
        :return: Um dicionário com as informações do processo.
        """

        response = None
        validate_entry = isinstance(data_date, str) and isinstance(country, str)

        if validate_entry:
            response = self.__covid_cases_repo.get_data(
                country=country, data_date=data_date
            )

        return {"success": validate_entry, "data": response}
