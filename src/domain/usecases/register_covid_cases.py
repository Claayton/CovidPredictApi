"""Interface para a classe RegisterCovidCases"""
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import CovidCases


class RegisterCovidCasesInterface(ABC):
    """Interface para a classe RegisterCovidCases"""

    @abstractmethod
    def register_covid_cases_by_country(self, country: str) -> Dict[bool, CovidCases]:
        """Deve ser implementado"""
        raise Exception("Deve ser implementado: register")
