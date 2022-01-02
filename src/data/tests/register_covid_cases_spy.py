"""Spy para a classe RegisterCovidCases"""
from typing import Dict
from src.domain.models import CovidCases
from src.domain.tests import mock_countries, mock_covid_cases


class RegisterCovidCasesSpy:
    """Classe para definir um Spy para a classe RegisterCovidCases"""

    def __init__(self, covid_cases_repo: any, get_countries: any) -> None:
        self.covid_cases_repo = covid_cases_repo
        self.get_countries = get_countries
        self.register_params = {}

    def register(
        self, date: str, new_cases: int, country: str
    ) -> Dict[bool, CovidCases]:
        """Registro de dados de casos de covid19 no banco de dados."""

        self.register_params["date"] = date
        self.register_params["new_cases"] = new_cases
        self.register_params["country"] = country

        response = None

        validate_entry = (
            isinstance(date, str)
            and isinstance(new_cases, int)
            and isinstance(country, str)
        )
        country_id = {"sucess": True, "data": [mock_countries()]}
        checker = (validate_entry) and (country_id is not None)

        if checker:
            response = mock_covid_cases()

        return {"success": checker, "data": response}
