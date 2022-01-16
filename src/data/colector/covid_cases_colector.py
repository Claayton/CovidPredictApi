"""Caso de uso para CovidCasesColector"""
from typing import List, Type, Dict
from src.data.interfaces import DataCovidConsumerInterface as DataCovidConsumer
from src.errors import HttpUnprocessableEntityError
from src.domain.usecases import (
    CovidCasesColectorInterface,
    GetCountriesInterface as GetCountries,
)


class CovidCasesColector(CovidCasesColectorInterface):
    """Caso de uso para CovidCasesColector"""

    def __init__(
        self, api_consumer: Type[DataCovidConsumer], get_countries: Type[GetCountries]
    ) -> None:
        self.__api_consumer = api_consumer
        self.__get_countries = get_countries

    def covid_cases_country(
        self, country: str, days: int = 0
    ) -> Dict[bool, List[Dict]]:
        """
        Realiza o tratamento dos dados do covid por país recebidos do consumer.
        :param country: O país de referência que deverá ser tratado os dados.
        :param days: A quantidade de dias futuros que devem ser previstos.
        :return: Os dados do covid19 ja tratados e com uma previsão para os próximos dias.
        """

        country_exist = self.__get_countries.by_name(name=country)

        if not country_exist["success"]:
            http_error = HttpUnprocessableEntityError(message="Invalid Country!")

            return {"success": False, "data": {"error": http_error}}

        api_response = self.__api_consumer.get_data_covid_by_country(country).response

        country_data_response = self.__separete_data(api_response, days, country)

        return {"success": True, "data": country_data_response}

    @classmethod
    def __separete_data(
        cls, data_days: List[Dict], days: int, country: str = None
    ) -> List[Dict]:

        separate_data = []

        for index, day in enumerate(data_days):

            try:
                separate_data.append(
                    {
                        "id": index + 1,
                        "date": day["date"],
                        "new_cases": day["new_cases"],
                        "country": country,
                        "days": days,
                    }
                )
            except KeyError:
                continue

        return separate_data
