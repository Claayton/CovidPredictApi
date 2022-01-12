"""Diretório de interface para controler"""
from typing import Dict, Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Interface Padrão para controllers"""

    @abstractmethod
    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Methodo para facilitar o request"""
        raise Exception("Should implement handler method")


class ControllersInterfaceList(ABC):
    """Interface de controller para list"""

    @abstractmethod
    def handler(self) -> Dict:
        """Methodo para facilitar o request"""
        raise Exception("Should implement handler method")


class ControllersInterfaceInfo(ABC):
    """Interface de controller para info"""

    @abstractmethod
    def handler(self, http_request: Dict) -> Dict:
        """Methodo para facilitar o request"""
        raise Exception("Should implement handler method")
