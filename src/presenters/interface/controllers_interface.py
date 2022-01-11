"""Diretório de interface para controler"""
from typing import Dict
from abc import ABC, abstractmethod


class ControllersInterfaceList(ABC):
    """Interface de controller"""

    @abstractmethod
    def handler(self) -> Dict:
        """Methodo para facilitar o request"""
        raise Exception("Should implement handler method")


class ControllersInterfaceInfo(ABC):
    """Interface de controller"""

    @abstractmethod
    def handler(self, http_request: Dict) -> Dict:
        """Methodo para facilitar o request"""
        raise Exception("Should implement handler method")
