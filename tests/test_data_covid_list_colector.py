from src.data.usecases.data_covid_list_colector import DataCovidListColector
from src.data.usecases.data_covid_list_colector import DataCovidListColector
from src.infra import DataCovidConsumer
from src import config

def test_list():
    api_consumer = DataCovidConsumer(config.SEARCH_URL)
    data_covid_list_colector = DataCovidListColector(api_consumer)

    data_covid_list_colector.list()
