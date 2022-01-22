"""Testes para countries_routes"""
from fastapi.testclient import TestClient
from faker import Faker
from src.infra.database.config import DataBaseConnectionHandler
from .countries_routes import countries

faker = Faker()
data_base_connection_handler = DataBaseConnectionHandler()
client = TestClient(countries)


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

    attributes = {"country": "Hogwarts"}
    url = f"/api/countries/?name={attributes['country']}"

    response = client.get(url)

    assert response.status_code == 422
    assert isinstance(response.json(), dict)
    assert "error" in response.json()["data"]


def test_register_country():
    """Testando a rota register_country"""

    attributes = {"name": faker.name().upper()}
    url = "/api/countries/single/"

    response = client.post(url=url, json=attributes)

    assert response.status_code == 200
    assert "data" in response.json()
    assert "error" not in response.json()

    engine = data_base_connection_handler.get_engine()
    engine.execute(f"DELETE FROM countries WHERE name='{attributes['name']}';")


def test_register_country_error_422():
    """Testando o erro 422 (Unprocessable Entity) na rota register_country"""

    url = "/api/countries/single/"

    response1 = client.post(url=url, json={"name": 25.5698})
    response2 = client.post(url=url, json={"name": "brasil"})
    response3 = client.post(url=url, json={"country": "BRA"})

    assert response1.status_code == 422
    assert response2.status_code == 422
    assert response3.status_code == 422

    assert "error" in response1.json()["data"]
    assert "error" in response2.json()["data"]
    assert "error" in response3.json()["data"]


def test_register_country_error_400():
    """Testando o erro 400 (Bad Request!) na rota register_country"""

    url = "/api/countries/single/"

    response = client.post(url=url)

    assert response.status_code == 400
    assert "error" in response.json()["data"]
