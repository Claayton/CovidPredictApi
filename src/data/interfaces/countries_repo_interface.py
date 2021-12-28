"""Interface para a classe CountryRepo"""
from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Country


class CountryRepoInterface(ABC):
    """Interface para CountryRepo"""

    @abstractmethod
    def insert_country(self, name: str) -> Country:
        """Método abstrato"""
        raise Exception("Método não implementado")

    @abstractmethod
    def get_countries(self) -> List[Country]:
        """Método abstrato"""
        raise Exception("Método não implementado")
