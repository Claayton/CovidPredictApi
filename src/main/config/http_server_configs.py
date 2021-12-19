"""Diretório de instância do app"""
from fastapi import FastAPI
from src.main.routes import data_covid_routes

app = FastAPI()

app.include_router(data_covid_routes)
