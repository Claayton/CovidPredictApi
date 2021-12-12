"""Testes relacionados a busca de dados na API"""
import requests
from src import config
from src.database.fetch_data import DadosCovid

def test_if_the_search_url_is_working():
    """Test if the search url is working"""
    response = requests.get(config.search_url)
    status = response.status_code
    assert status == 200

def test_if_fetch_data_by_country_is_working():
    """Test if the search data by country is working"""
    dc = DadosCovid(config.search_url, "BRA")
    response = dc.fetch_data_by_country("BRA")
    assert response[0]['new_cases'] == 1.0

def test_if_fetch_data_from_world_is_working():
    """Test if the search data from world is working"""
    dc = DadosCovid(config.search_url, "BRA")
    response = dc.fetch_data_from_world()
    assert response[0][0]['new_cases'] == 5.0
