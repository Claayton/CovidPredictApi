"""Testes relacionados a busca de dados na API"""
from src.infra.data_covid_consumer import DataCovidConsumer
from src import config
from src.errors import HttpRequestError

def test_get_data_covid(requests_mock):
    """Test if the search data by country is working"""

    url = config.SEARCH_URL
    country = ['BRA']

    requests_mock.get(
        url=url,
        status_code = 200,
        json = {'some': 'thing', country[0]: {'data': [{}]}}
    )

    data_covid_consumer = DataCovidConsumer(url)
    get_data_covid_response = data_covid_consumer.get_data_covid()

    assert get_data_covid_response.request.method == 'GET'
    assert get_data_covid_response.request.url == url

    assert get_data_covid_response.status_code == 200
    assert isinstance(get_data_covid_response.response['BRA']['data'], list)

def test_get_data_covid_http_error(requests_mock):
    """Teste de erro em get_data_covid"""

    url = f'{config.SEARCH_URL}CASCAVEL'

    requests_mock.get(
        url=url,
        status_code = 404,
        json = {'details': 'somenthing'}
    )

    data_covid_consumer = DataCovidConsumer(url)
    try:
        data_covid_consumer.get_data_covid()
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None

def test_get_data_covid_information(requests_mock):
    """Testando o metodo get_data_covid_information"""

    country = 'BRA'
    data_covid_consumer = DataCovidConsumer(config.SEARCH_URL)

    requests_mock.get(
        url=config.SEARCH_URL,
        status_code=200,
        json={
            "BRA": {
                'data': [{
                    'date': '2021-09-15',
                    'total_cases': 21034610.0,
                    'new_cases': 14780.0,
                    'total_deaths': 588597.0
                }]
            }
        }
    )

    data_covid_information = data_covid_consumer.get_data_covid_information(country)

    assert data_covid_information.request.method == 'GET'
    assert data_covid_information.request.url == config.SEARCH_URL
    assert data_covid_information.status_code == 200

    assert 'total_deaths' in data_covid_information.response[0]

def test_get_data_covid_information_error(requests_mock):
    """Testando o metodo get_data_covid_information in error"""

    country = 'BRA'
    data_covid_consumer = DataCovidConsumer(config.SEARCH_URL)

    requests_mock.get(
        url=config.SEARCH_URL,
        status_code=404,
        json={'details': 'something'}
    )

    try:
        data_covid_consumer.get_data_covid_information(country)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
