"""Diretório de instância do app"""
from fastapi import FastAPI
from src.main.routes import countries_routes

app = FastAPI()

app.include_router(countries_routes)
