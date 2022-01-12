"""Diretório de casos de uso - Coletor de interface de dados covid"""
from abc import ABC, abstractmethod
from typing import Dict, List


class CovidCasesColectorInterface(ABC):
    """Coletor de Interface de informações do dados covid"""

    @abstractmethod
    def covid_cases_country(
        self, country: str, days: int = 0
    ) -> Dict[bool, List[Dict]]:
        """Deve ser implementado"""
        raise Exception("Must implement find_country method")

    @abstractmethod
    def covid_cases_world(self, days: int) -> Dict[bool, List[Dict]]:
        """Deve ser implementado"""
        raise Exception("Must implement find_country method")
