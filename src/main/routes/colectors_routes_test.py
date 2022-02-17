"""Testes para colectors_routes"""
from fastapi.testclient import TestClient
from .colectors_routes import colectors

client = TestClient(colectors)


def test_colector():
    """Testando a rota colector"""

    url = "/api/colectors/covid_cases/direct/?country=BRA"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "new_cases" in response.json()["data"][0]
    assert "country" in response.json()["data"][0]


def test_colector_error_422():
    """
    Testando o erro 400 (BadRequest) na rota colector.
    Utilizando um valor inválido para o parâmetro de query 'country'.
    """

    url = "/api/colectors/covid_cases/direct/?country=123"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_colector_error_400():
    """
    Testando o erro 400 (BadRequest) na rota colector.
    Sem utilizar nenhum parâmetro de query.
    """

    url = "/api/colectors/covid_cases/direct/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 400
    assert "error" in response.json()["data"]


def test_register_countries():
    """Testando a rota register_countries"""

    url = "/api/colectors/countries/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert "data" in response.json()
    assert "error" not in response.json()


def test_register_covid_cases():
    """Testando a rota register_covid_cases"""

    url = "/api/colectors/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "date" in response.json()["data"]["BRA"][0]
    assert "new_cases" in response.json()["data"]["BRA"][0]
    assert "data" in response.json()
    assert "error" not in response.json()
