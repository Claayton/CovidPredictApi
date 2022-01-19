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

    @abstractmethod
    def by_id(self, country_id: int) -> Dict[bool, List[Country]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método by_name")

    @abstractmethod
    def all_countries(self) -> Dict[bool, List[Country]]:
        """Caso de uso específico"""

        raise Exception("Deve ser implementado o método all")
