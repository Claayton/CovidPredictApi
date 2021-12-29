"""Interface para a classe GetCountries"""
from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Country


class GetCountriesInterface(ABC):
    """Interface para a classe GetCountries"""

    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, List[Country]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método by_name")

    @classmethod
    def all_countries(cls) -> Dict[bool, List[Country]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método all")
