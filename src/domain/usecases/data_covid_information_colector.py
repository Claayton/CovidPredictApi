"""Diretório de casos de uso - Coletor de interface de dados covid"""
from abc import ABC, abstractmethod
from typing import Dict

class DataCovidInformationColectorInterface(ABC):
    """Coletor de Interface de informações do dados covid"""

    @abstractmethod
    def find_country(self, country: str, time: int) -> Dict:
        """Deve ser implementado"""
        raise Exception('Must implement find_country method')
