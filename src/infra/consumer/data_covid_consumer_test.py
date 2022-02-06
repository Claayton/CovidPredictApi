"""Testes para a classe DataCovidConsumer"""
from src import config
from src.errors import HttpRequestError
from .data_covid_consumer import DataCovidConsumer


def test_get_countries(requests_mock):
    """Testando o método get_countries"""

    url = config.SEARCH_URL

    requests_mock.get(
        url=url, status_code=200, json={"BRA": {"data": [{}]}, "USA": {"data": [{}]}}
    )

    data_covid_consumer = DataCovidConsumer(url)
    get_countries_response = data_covid_consumer.get_countries()

    # Testando os requests:
    assert get_countries_response.request.method == "GET"
    assert get_countries_response.request.url == url

    # Testando os responses:
    assert get_countries_response.status_code == 200
    assert isinstance(get_countries_response.response, list)


def test_get_countries_http_error(requests_mock):
    """Testando o erro no método get_countries."""

    url = config.SEARCH_URL

    requests_mock.get(url=url, status_code=404, json={"error": "deu ruim"})

    data_covid_consumer = DataCovidConsumer(url)

    try:
        data_covid_consumer.get_countries()
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert (error.status_code < 200) or (error.status_code > 299)


def test_get_all_data_covid(requests_mock):
    """Testando o método get_all_data_covid"""

    url = config.SEARCH_URL

    requests_mock.get(
        url=url, status_code=200, json={"BRA": {"data": [{}]}, "USA": {"data": [{}]}}
    )

    data_covid_consumer = DataCovidConsumer(url)
    get_all_data_covid_response = data_covid_consumer.get_all_data_covid()

    # Testando o request:
    assert get_all_data_covid_response.request.method == "GET"
    assert get_all_data_covid_response.request.url == url

    # Testando o response:
    assert get_all_data_covid_response.status_code == 200
    assert isinstance(get_all_data_covid_response.response, dict)


def test_get_all_data_covid_http_error(requests_mock):
    """Testando o erro no método get_all_data_covid"""

    url = f"{config.SEARCH_URL}CASCAVEL"

    requests_mock.get(url=url, status_code=404, json={"error": "deu ruim"})

    data_covid_consumer = DataCovidConsumer(url)

    try:
        data_covid_consumer.get_all_data_covid()
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert (error.status_code < 200) or (error.status_code > 299)


def test_get_data_covid_by_country(requests_mock):
    """Testando o método test_get_data_covid_by_country"""

    country = "BRA"
    url = config.SEARCH_URL

    requests_mock.get(
        url=config.SEARCH_URL,
        status_code=200,
        json={
            "BRA": {
                "data": [
                    {
                        "date": "2021-09-15",
                        "total_cases": 21034610.0,
                        "new_cases": 14780.0,
                        "total_deaths": 588597.0,
                    }
                ]
            }
        },
    )

    data_covid_consumer = DataCovidConsumer(url)
    data_covid_by_country_response = data_covid_consumer.get_data_covid_by_country(
        country=country
    )

    # Testando o request:
    assert data_covid_by_country_response.request.method == "GET"
    assert data_covid_by_country_response.request.url == url

    # Testando o response:
    assert data_covid_by_country_response.status_code == 200
    assert isinstance(data_covid_by_country_response.response, list)
    assert isinstance(data_covid_by_country_response.response[0], dict)
    assert "new_cases" in data_covid_by_country_response.response[0]


def test_get_data_covid_by_country_http_error(requests_mock):
    """Testando o erro no método get_data_covid_by_country"""

    country = "BRA"
    url = f"{config.SEARCH_URL}CASCAVEL"

    requests_mock.get(url=url, status_code=404, json={"error": "deu ruim"})

    data_covid_consumer = DataCovidConsumer(url)

    try:
        data_covid_consumer.get_data_covid_by_country(country)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert (error.status_code < 200) or (error.status_code > 299)
