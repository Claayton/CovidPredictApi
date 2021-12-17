"""Diretório de casos de uso - Coletor de interface de dados covid"""
from abc import ABC, abstractmethod
from typing import Dict, List

class DataCovidListColectorInterface(ABC):
    """Coletor de Interface de dados covid"""

    @abstractmethod
    def list(self) -> List[Dict]:
        """Deve ser implementado"""
        raise Exception('Must implement list method')
