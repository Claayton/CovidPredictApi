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

    url = f'{config.SEARCH_URL}BRA'
    country = ['BRA']

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
