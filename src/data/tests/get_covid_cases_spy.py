"""Classe Spy para GetCovidCases"""
from typing import Dict, List
from src.domain.models import CovidCases
from src.domain.tests import mock_covid_cases


class GetCovidCasesSpy:
    """Classe para definir o caso de uso: GetCovidCases"""

    def __init__(self, covid_cases_repo: any) -> None:
        self.countries_repo = covid_cases_repo
        self.by_country_and_by_date_params = {}
        self.by_country_params = {}
        self.by_date_params = {}

    def by_country(self, country: str) -> Dict[bool, List[CovidCases]]:
        """
        Realiza a busca dos casos de covid19 por país.
        :param country: Abreviação do nome do país.
        :return: Um dicionário com as informações do processo.
        """
        self.by_country_params["country"] = country

        response = None
        validate_entry = isinstance(country, str)

        if validate_entry:
            response = mock_covid_cases()

        return {"success": validate_entry, "data": response}

    def by_date(self, data_date: str) -> Dict[bool, List[CovidCases]]:
        """
        Realiza a busca dos casos de covid19 por data.
        :param data_date: Data para a busca.
        :return: Um dicionário com as informações do processo.
        """

        self.by_date_params["date"] = data_date

        response = None
        validate_entry = isinstance(data_date, str)

        if validate_entry:
            response = mock_covid_cases()

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

        self.by_country_and_by_date_params["country"] = country
        self.by_country_and_by_date_params["date"] = data_date

        response = None
        validate_entry = isinstance(data_date, str) and isinstance(country, str)

        if validate_entry:
            response = mock_covid_cases()

        return {"success": validate_entry, "data": response}
