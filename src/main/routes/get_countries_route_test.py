"""Testes para countries_routes"""
from fastapi.testclient import TestClient
from .get_countries_route import countries_routes

client = TestClient(countries_routes)


def test_get_countries_no_query():
    """Testando a rota get_countries sem utilizar parâmetro de query no url"""

    url = "/api/countries/"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "id" in response.json()["data"][0]
    assert "name" in response.json()["data"][0]


def test_get_countries_with_query():
    """Testando a rota get_countries utilizando um parâmetro de query no url"""

    attributes = {"country": "BRA"}
    url = f"/api/countries/?name={attributes['country']}"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "id" in response.json()["data"][0]
    assert "name" in response.json()["data"][0]


def test_get_countries_error_422():
    """Testando o erro 422 (Unprocessable Entity) na rota get_countries"""

    attributes = {"country": "CASCAVEL"}
    url = f"/api/countries/?name={attributes['country']}"

    response = client.get(url)

    assert response.status_code == 422
    assert isinstance(response.json(), dict)
    assert "error" in response.json()["data"]
