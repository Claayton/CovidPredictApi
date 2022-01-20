"""Testes para covid_cases_colector_routes"""
from fastapi.testclient import TestClient
from .covid_cases_colector_route import covid_cases_colector_routes

client = TestClient(covid_cases_colector_routes)


def test_colector():
    """Testando a rota colector"""

    url = "/api/colector/?country=BRA"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "new_cases" in response.json()["data"][0]
    assert "country" in response.json()["data"][0]


def test_colector_error_400():
    """Testando o erro 400 (BadRequest) na rota colector"""

    url = "/api/colector/"

    response = client.get(url)

    assert response.status_code == 400
    assert "error" in response.json()["data"]
