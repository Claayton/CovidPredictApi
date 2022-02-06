"""Testes para countries_routes"""
from fastapi.testclient import TestClient
from faker import Faker
from .countries_routes import countries

faker = Faker()
client = TestClient(countries)


def test_get_countries_without_query_params():
    """
    Testando a rota get_countries.
    Sem utilizar nenhum parâmetro de query no url.
    """

    url = "/api/countries/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "id" in response.json()["data"][0]
    assert "name" in response.json()["data"][0]


def test_get_countries_with_query_params():
    """
    Testando a rota get_countries.
    Utilizando um valor válido para o parâmetro de query 'country' no url.
    """

    attributes = {"country": "BRA"}

    url = f"/api/countries/?name={attributes['country']}"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "id" in response.json()["data"][0]
    assert "name" in response.json()["data"][0]


def test_get_countries_error_422():
    """
    Testando o erro 422 (Unprocessable Entity) na rota get_countries.
    Utilizando um valor inválido para o parâmetro de query 'country' no url.
    """

    attributes = {"country": "Hogwarts"}

    url = f"/api/countries/?name={attributes['country']}"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 422
    assert isinstance(response.json(), dict)
    assert "error" in response.json()["data"]


def test_register_countries():
    """Testando a rota register_countries"""

    url = "/api/countries/"
    headers = {"X-Test": "true"}

    response = client.post(url=url, headers=headers)

    assert response.status_code == 200
    assert "data" in response.json()
    assert "error" not in response.json()
