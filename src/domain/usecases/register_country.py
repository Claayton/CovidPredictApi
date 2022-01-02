"""Interface para a classe RegisterCountry"""
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Country


class RegisterCountryInterface(ABC):
    """Interface para a classe RegisterCountry"""

    @abstractmethod
    def register(self, name: str) -> Dict[bool, Country]:
        """Deve ser implementado"""
        raise Exception("Deve ser implementado: register")
