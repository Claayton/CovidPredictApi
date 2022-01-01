"""Interface para a classe RegisterCovidCases"""
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import CovidCases


class RegisterCovidCasesInterface(ABC):
    """Interface para a classe RegisterCovidCases"""

    @abstractmethod
    def register(
        self, date: str, new_cases: int, country: str
    ) -> Dict[bool, CovidCases]:
        """Deve ser implementado"""
        raise Exception("Deve ser implementado: register")
