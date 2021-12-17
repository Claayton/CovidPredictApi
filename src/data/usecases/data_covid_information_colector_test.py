"""Testes para data_covid_information_colector"""
from src.data.usecases.data_covid_information_colector import DataCovidInformationColector
from src.infra.tests.data_covid_consumer import DataCovidConsumerSpy

def test_find_country():
    """Testando p metodo find_country"""

    api_consumer = DataCovidConsumerSpy()
    data_covid_information_colector = DataCovidInformationColector(api_consumer)

    country = 'BRA'
    time = 4

    response = data_covid_information_colector.find_country(country, time)

    assert api_consumer.get_data_covid_information_attributes['country'] == country
    assert isinstance(response, list)
    assert 'new_cases_real' in response[0]
    assert 'predicted_evolution' in response[0]
