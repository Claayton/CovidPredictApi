"""Diretório de instância do app"""
from fastapi import FastAPI
from src.main.routes import (
    countries_routes,
    covid_cases_routes,
    covid_cases_colector_routes,
)


def create_app() -> FastAPI:
    """Função para criar o app"""

    app = FastAPI()

    app.include_router(countries_routes)
    app.include_router(covid_cases_routes)
    app.include_router(covid_cases_colector_routes)

    return app
