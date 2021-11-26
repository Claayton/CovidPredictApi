"""Testes relacionados a busca de dados na API"""
import requests
from app import config

def test_if_the_search_url_is_working():
    """Test if the search url is working"""
    response = requests.get(config.search_url)
    status = response.status_code
    assert status == 200
