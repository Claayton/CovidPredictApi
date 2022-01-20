"""Testes para covid_cases_predict_routes"""
from fastapi.testclient import TestClient
from .covid_cases_predict_route import covid_cases_predict_routes

client = TestClient(covid_cases_predict_routes)


def test_predict():
    """Testando a rota predict"""

    url = "/api/predict/?country=BRA&days=5"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "new_cases_real" in response.json()["data"][0]
    assert "country" in response.json()["data"][0]


def test_predict_error_422():
    """Testando o erro 422 (HttpUnprocessableEntity) na rota predict"""

    url = "/api/predict/"

    response1 = client.get(url)
    response2 = client.get(f"{url}?country=BRA")
    response3 = client.get(f"{url}?country=CASCAVEL")
    response4 = client.get(f"{url}?days=23")
    response5 = client.get(f"{url}?days=macarena")

    assert response1.status_code == 422
    assert response2.status_code == 422
    assert response3.status_code == 422
    assert response4.status_code == 422
    assert response5.status_code == 422

    assert "error" in response1.json()["data"]
    assert "error" in response2.json()["data"]
    assert "error" in response3.json()["data"]
    assert "error" in response4.json()["data"]
    assert "error" in response5.json()["data"]
