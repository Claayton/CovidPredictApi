"""Testes para covid_cases_routes"""
from fastapi.testclient import TestClient
from .covid_cases_routes import covid_cases

client = TestClient(covid_cases)


def test_get_covid_cases_without_query_params():
    """
    Testando a rota get_covid_cases.
    Sem utilizar nenhum parâmetro de query no url.
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "date" in response.json()["data"][0]
    assert "new_cases" in response.json()["data"][0]


def test_get_covid_cases_with_date_query_param():
    """
    Testando a rota get_covid_cases.
    Utilizando um valor válido para o parâmetro de query 'date' no url
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?date=2021-12-31", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "date" in response.json()["data"][0]
    assert "new_cases" in response.json()["data"][0]


def test_get_covid_cases_with_country_query_param():
    """
    Testando a rota get_covid_cases.
    Utilizando um valor válido para o parâmetro de query 'country' no url
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?country=BRA", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "date" in response.json()["data"][0]
    assert "new_cases" in response.json()["data"][0]


def test_get_covid_cases_with_date_and_country_query_params():
    """
    Testando a rota get_covid_cases.
    Utilizando valores válidos para os parâmetros de query 'date' e 'country' no url
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?date=2021-12-31&country=BRA", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "date" in response.json()["data"][0]
    assert "new_cases" in response.json()["data"][0]


def test_get_covid_cases_error_422_1():
    """
    Testando o erro 422 (Unprocessable Entity) na rota get_covid_cases.
    Utilizando um parâmetro de query inválido.
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?h2n3=true", headers=headers)

    assert response.status_code == 422
    assert isinstance(response.json(), dict)
    assert "error" in response.json()["data"]


def test_get_covid_cases_error_422_2():
    """
    Testando o erro 422 (Unprocessable Entity) na rota get_covid_cases.
    Utilizando um valor inválido para o parâmetro de query 'country'.
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?country=CASCAVEL", headers=headers)

    assert response.status_code == 422
    assert isinstance(response.json(), dict)
    assert "error" in response.json()["data"]


def test_get_covid_cases_error_422_3():
    """
    Testando o erro 422 (Unprocessable Entity) na rota get_covid_cases.
    Utilizando um valor inválido para o parâmetro de query 'date'.
    """

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?date=margarina", headers=headers)

    assert response.status_code == 422
    assert isinstance(response.json(), dict)
    assert "error" in response.json()["data"]


def test_register_covid_cases():
    """Testando a rota register_covid_cases"""

    url = "/api/covid_cases/"
    headers = {"X-Test": "true"}

    response = client.post(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "date" in response.json()["data"]["BRA"][0]
    assert "new_cases" in response.json()["data"]["BRA"][0]
    assert "data" in response.json()
    assert "error" not in response.json()


def test_predict():
    """Testando a rota predict"""

    url = "/api/covid_cases/predict/?country=BRA&days=5"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "new_cases_real" in response.json()["data"][0]
    assert "country" in response.json()["data"][0]


def test_predict_error_422_1():
    """
    Testando o erro 422 (HttpUnprocessableEntity) na rota predict.
    Sem utilizar nenhum parâmetro de query.
    """

    url = "/api/covid_cases/predict/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_predict_error_422_2():
    """
    Testando o erro 422 (HttpUnprocessableEntity) na rota predict.
    Utilizando apenas o parâmetro de query 'country'.
    """

    url = "/api/covid_cases/predict/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?country=BRA", headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_predict_error_422_3():
    """
    Testando o erro 422 (HttpUnprocessableEntity) na rota predict.
    Utilizando apenas o parâmetro de query 'days'.
    """

    url = "/api/covid_cases/predict/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?days=5", headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_predict_error_422_4():
    """
    Testando o erro 422 (HttpUnprocessableEntity) na rota predict.
    Utilizando um valor inválido para o parâmetro de query 'country'.
    """

    url = "/api/covid_cases/predict/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?country=CASCAVEL&days=5", headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_predict_error_422_5():
    """
    Testando o erro 422 (HttpUnprocessableEntity) na rota predict.
    Utilizando um valor inválido para o parâmetro de query 'days'.
    """

    url = "/api/covid_cases/predict/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?country=BRA&days=macarena", headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_predict_error_422_6():
    """
    Testando o erro 422 (HttpUnprocessableEntity) na rota predict.
    Utilizando apenas valores inválidos para o parâmetros de query 'country' e 'days'.
    """

    url = "/api/covid_cases/predict/"
    headers = {"X-Test": "true"}

    response = client.get(url=f"{url}?country=CASCAVEL&days=macarena", headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


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


def test_colector_error_422():
    """
    Testando o erro 400 (BadRequest) na rota colector.
    Utilizando um valor inválido para o parâmetro de query 'country'.
    """

    url = "/api/covid_cases/colector/?country=123"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 422
    assert "error" in response.json()["data"]


def test_colector_error_400():
    """
    Testando o erro 400 (BadRequest) na rota colector.
    Sem utilizar nenhum parâmetro de query.
    """

    url = "/api/covid_cases/colector/"
    headers = {"X-Test": "true"}

    response = client.get(url=url, headers=headers)

    assert response.status_code == 400
    assert "error" in response.json()["data"]
