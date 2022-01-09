"""Interface para a classe CovidCasePredict"""
from abc import ABC, abstractmethod
from typing import Dict, List


class CovidCasesPredictInterface(ABC):
    """Interface para a classe CovidCasePredict"""

    @abstractmethod
    def covid_evolution_predict(self, country: str, days: int) -> List[Dict]:
        """Deve ser implementado"""
        raise Exception("Must implement list method")
