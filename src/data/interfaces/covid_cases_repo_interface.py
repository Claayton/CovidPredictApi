"""Interface para a classe CovidCasesRepo"""
from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.models import CovidCases


class CovidCasesRepoInterface(ABC):
    """Interface para CovidCasesRepo"""

    @abstractmethod
    def insert_data(self, data_date: str, new_cases: int, country: str) -> CovidCases:
        """Método abstrato"""
        raise Exception("Método não implementado")

    @abstractmethod
    def update_cases(self, cases_id: int, new_cases: int) -> CovidCases:
        """Método abstrato"""
        raise Exception("Método não implementado")

    @abstractmethod
    def get_data(self, country: str = None, data_date: str = None) -> List[Tuple]:
        """Método abstrato"""
        raise Exception("Método não implementado")
