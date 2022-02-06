"""Spy para a classe RegisterCovidCases"""
from typing import Dict
from src.domain.models import CovidCases
from src.domain.tests import mock_covid_cases


class RegisterCovidCasesSpy:
    """Classe para definir um Spy para a classe RegisterCovidCases"""

    @classmethod
    def register_covid_cases(cls) -> Dict[bool, CovidCases]:
        """
        Registro de dados de todos casos de covid19 vindos da API, no banco de dados.
        :return: Um dicionário com as informações do processo.
        """

        response = mock_covid_cases()

        return {"success": True, "data": response}
