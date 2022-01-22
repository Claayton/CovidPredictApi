"""Testes para covid_cases_routes"""
from fastapi.testclient import TestClient
from .covid_cases_routes import covid_cases

client = TestClient(covid_cases)


def test_get_covid_cases_no_query():
    """Testando a rota get_covid_cases sem utilizar parâmetro de query no url"""

    url = "/api/covid_cases/"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "date" in response.json()["data"][0]
    assert "new_cases" in response.json()["data"][0]


def test_get_covid_cases_with_query():
    """Testando a rota get_covid_cases utilizando parâmetros de query no url"""

    url = "/api/covid_cases/"

    response1 = client.get(f"{url}?date=2021-12-31")
    response2 = client.get(f"{url}?country=WORLD")
    response3 = client.get(f"{url}?date=2021-12-31&country=WORLD")

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200

    assert isinstance(response1.json(), dict)
    assert isinstance(response2.json(), dict)
    assert isinstance(response3.json(), dict)

    assert isinstance(response1.json()["data"], list)
    assert isinstance(response2.json()["data"], list)
    assert isinstance(response3.json()["data"], list)

    assert "date" in response1.json()["data"][0]
    assert "date" in response2.json()["data"][0]
    assert "date" in response3.json()["data"][0]

    assert "new_cases" in response1.json()["data"][0]
    assert "new_cases" in response2.json()["data"][0]
    assert "new_cases" in response3.json()["data"][0]


def test_get_covid_cases_error_422():
    """Testando o erro 422 (Unprocessable Entity) na rota get_covid_cases"""

    url = "/api/covid_cases/"

    response1 = client.get(f"{url}?h2n3=true")
    response2 = client.get(f"{url}?country=CASCAVEL")
    response3 = client.get(f"{url}?date=margarina")

    assert response1.status_code == 422
    assert response2.status_code == 422
    assert response3.status_code == 422

    assert isinstance(response1.json(), dict)
    assert isinstance(response2.json(), dict)
    assert isinstance(response3.json(), dict)

    assert "error" in response1.json()["data"]
    assert "error" in response2.json()["data"]
    assert "error" in response3.json()["data"]


def test_predict():
    """Testando a rota predict"""

    url = "/api/covid_cases/predict/?country=BRA&days=5"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "new_cases_real" in response.json()["data"][0]
    assert "country" in response.json()["data"][0]


def test_predict_error_422():
    """Testando o erro 422 (HttpUnprocessableEntity) na rota predict"""

    url = "/api/covid_cases/predict/"

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


def test_colector():
    """Testando a rota colector"""

    url = "/api/covid_cases/colector/?country=BRA"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "new_cases" in response.json()["data"][0]
    assert "country" in response.json()["data"][0]


def test_colector_error_400():
    """Testando o erro 400 (BadRequest) na rota colector"""

    url = "/api/covid_cases/colector/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 400
    assert "error" in response.json()["data"]
