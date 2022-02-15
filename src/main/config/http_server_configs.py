"""Diretório de instância do app"""
from fastapi import FastAPI
from src.main.routes import countries, covid_cases
from ..docs import tags_metadata


def create_app() -> FastAPI:
    """Função para criar o app"""

    app = FastAPI(
        title="CovidPredictApi",
        description="Api de dados sobre o covid 19 no mundo",
        version="0.0.1",
        openapi_tags=tags_metadata,
    )

    app.include_router(countries)
    app.include_router(covid_cases)

    return app
