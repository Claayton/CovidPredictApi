"""Diretório de interface para controler"""
from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Interface Padrão para controllers"""

    @abstractmethod
    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Methodo para facilitar o request"""
        raise Exception("Should implement handler method")
