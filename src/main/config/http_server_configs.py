"""Diretório de instância do app"""
from fastapi import FastAPI
from src.main.routes import countries, covid_cases


def create_app() -> FastAPI:
    """Função para criar o app"""

    app = FastAPI()

    app.include_router(countries)
    app.include_router(covid_cases)

    return app
