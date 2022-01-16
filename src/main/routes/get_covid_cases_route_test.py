"""Testes para covid_cases_routes"""
from fastapi.testclient import TestClient
from .get_covid_cases_route import covid_cases_routes

client = TestClient(covid_cases_routes)


def test_get_data_covid_from_country_no_query():
    """Testando a rota get_data_covid_from_country sem utilizar parâmetro de query no url"""

    url = "/api/covid_cases/"

    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert isinstance(response.json()[0], dict)
    assert "date" in response.json()[0]
    assert "new_cases" in response.json()[0]


def test_get_data_covid_from_country_with_query():
    """Testando a rota get_data_covid_from_country utilizando parâmetros de query no url"""

    url = "/api/covid_cases/"

    response1 = client.get(f"{url}?date=2021-12-31")
    response2 = client.get(f"{url}?country=WORLD")
    response3 = client.get(f"{url}?date=2021-12-31&country=WORLD")

    assert response1.status_code == 200
    assert isinstance(response1.json(), list)
    assert isinstance(response1.json()[0], dict)
    assert "date" in response1.json()[0]
    assert "new_cases" in response1.json()[0]

    assert response2.status_code == 200
    assert isinstance(response2.json(), list)
    assert isinstance(response2.json()[0], dict)
    assert "date" in response2.json()[0]
    assert "new_cases" in response2.json()[0]

    assert response3.status_code == 200
    assert isinstance(response3.json(), list)
    assert isinstance(response3.json()[0], dict)
    assert "date" in response3.json()[0]
    assert "new_cases" in response3.json()[0]


def test_get_data_covid_from_country_error_422():
    """Testando o erro 422 (Unprocessable Entity) na rota get_data_covid_from_country"""

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

    assert "error" in response1.json()
    assert "error" in response2.json()
    assert "error" in response3.json()
