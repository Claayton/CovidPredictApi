"""Testes relacionados a busca de dados na API"""
from src.database.fetch_data import DataCovidConsumer

# def test_url(requests_mock):
#     requests_mock.get('http://google.com', text='data')
#     assert 'data' == requests.get('http://google.com').text

def test_get_data_covid():
    """Test if the search data by country is working"""

    # requests_mock.get(
    #     'https://covid.ourworldindata.org/data/owid-covid-data.json/',
    #     status_code = 200,
    #     json = {"some": "thing"}
    # )
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.json/'

    data_covid_consumer = DataCovidConsumer("BRA")
    get_data_covid_response = data_covid_consumer.get_data_covid()

    assert get_data_covid_response.request.method == 'GET'
    assert get_data_covid_response.request.url == url

    assert get_data_covid_response.status_code == 200
    assert isinstance(get_data_covid_response.response['BRA']['data'], list)

# def test_if_fetch_data_from_world_is_working():
#     """Test if the search data from world is working"""
#     dc = DadosCovid(config.search_url, "BRA")
#     response = dc.fetch_data_from_world()
#     assert response[0][0]['new_cases'] == 5.0
