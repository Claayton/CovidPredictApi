"""Diretório para Dominio e casos de uso"""
from typing import List, Dict, Type
from src.domain.usecases import DataCovidListColectorInterface
from src.data.interfaces.data_covid_consumer import DataCovidConsumerInterface


class DataCovidListColector(DataCovidListColectorInterface):
    """Casos de uso para DataCovidListColector"""

    def __init__(self, api_consumer: Type[DataCovidConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, country: List[str]) -> List[Dict]:
        api_response = self.__api_consumer.get_data_covid()
        data_covid_formated_list = self.__format_api_response(
            api_response.response[country[0]]['data']
        )
        return data_covid_formated_list

    @classmethod
    def __format_api_response(cls, api_response: List[Dict]) -> List[Dict]:
        data_covid_formated_list = []

        for index, day in enumerate(api_response):
            try:
                data_covid_formated_list.append(
                    {
                        "id": index,
                        "date": day["date"],
                        "new_cases": day["new_cases"]
                    }
                )
            except KeyError:
                continue
        return data_covid_formated_list
  