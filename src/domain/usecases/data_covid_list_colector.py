from abc import ABC, abstractmethod
from typing import Dict

class DataCovidListColectorInterface(ABC):
    """Coletor de Interface de dados covid"""

    @abstractmethod
    def list(self) -> Dict:
        """Deve ser implementado"""
        raise Exception('Must implement list method')
