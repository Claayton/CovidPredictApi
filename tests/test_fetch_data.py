"""Testes relacionados a busca de dados na API"""
from src.infra.data_covid_consumer import DataCovidConsumer
from src import config
from src.errors import HttpRequestError

def test_get_data_covid(requests_mock):
    """Test if the search data by country is working"""

    url = config.SEARCH_URL
    requests_mock.get(
        url=url,
        status_code = 200,
        json = {'some': 'thing', 'BRA': {'data': [{}]}}
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


# def test_if_fetch_data_from_world_is_working():
#     """Test if the search data from world is working"""
#     dc = DadosCovid(config.search_url, "BRA")
#     response = dc.fetch_data_from_world()
#     assert response[0][0]['new_cases'] == 5.0
