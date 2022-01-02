"""Interface para a classe GetCovidCases"""
from abc import ABC, abstractmethod
from datetime import date
from typing import Dict, List, Type
from src.domain.models import CovidCases


class GetCovidCasesInterface(ABC):
    """Interface para a classe GetCovidCases"""

    @abstractmethod
    def by_country(self, country: str) -> Dict[bool, List[CovidCases]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método by_country")

    @abstractmethod
    def by_date(self, data_date: Type[date]) -> Dict[bool, List[CovidCases]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método by_date")

    @abstractmethod
    def by_country_and_by_date(
        self, country: str, data_date: Type[date]
    ) -> Dict[bool, List[CovidCases]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método by_country_and_by_date")
