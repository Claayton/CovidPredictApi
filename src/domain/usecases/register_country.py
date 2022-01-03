"""Interface para a classe RegisterCountry"""
from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Country


class RegisterCountryInterface(ABC):
    """Interface para a classe RegisterCountry"""

    @abstractmethod
    def register_country(self, name: str) -> Dict[bool, Country]:
        """Deve ser implementado"""
        raise Exception("Deve ser implementado: register")

    @abstractmethod
    def register_countries(self) -> Dict[bool, List[Country]]:
        """Deve ser implementado"""
        raise Exception("Deve ser implementado: register")
