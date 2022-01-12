"""Testes para countries_routes"""
from fastapi.testclient import TestClient
from .get_countries_route import countries_routes

client = TestClient(countries_routes)


def test_get_countries_no_query():
    """Testando a rota get_countries sem utilizar parâmetro de query no url"""

    url = "/api/countries/"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert isinstance(response.json()[0], dict)
    assert "id" in response.json()[0]
    assert "name" in response.json()[0]


def test_get_countries_with_query():
    """Testando a rota get_countries utilizando um parâmetro de query no url"""

    attributes = {"country": "BRA"}
    url = f"/api/countries/?name={attributes['country']}"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert isinstance(response.json()[0], dict)
    assert "id" in response.json()[0]
    assert "name" in response.json()[0]


def test_get_countries_error_400():
    """Testando o erro 400 (BadRequest) na rota get_countries"""

    attributes = {"country": "CASCAVEL"}
    url = f"/api/countries/?name={attributes['country']}"

    response = client.get(url)

    assert response.status_code == 400
    assert isinstance(response.json(), dict)
    assert "error" in response.json()
