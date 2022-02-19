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

    def covid_cases_colector(self, country: str = None) -> Dict[bool, List[Dict]]:
        """
        Realiza o tratamento dos dados do covid por país recebidos do consumer.
        :param country: O país de referência que deverá ser tratado os dados.
            * por padão o parametro country é None, retornando os dados de todos os países.
        :return: Os dados do covid19 (data, casos no dia), separados em dicionarios.
        """

        if country is not None:

            country_exist = self.__get_countries.by_name(name=country)

            if not country_exist["success"]:
                http_error = HttpUnprocessableEntityError(message="Invalid Country!")

                return {"success": False, "data": {"error": http_error}}

            api_response = self.__api_consumer.get_data_covid_by_country(
                country
            ).response
            country_data_response = self.__separete_country_data(api_response, country)

            return {"success": True, "data": country_data_response}

        api_response = self.__api_consumer.get_all_data_covid()
        all_data_response = self.__separete_all_data(api_response=api_response.response)

        return {"success": True, "data": all_data_response}

    @classmethod
    def __separete_country_data(
        cls, data_days: List[Dict], country: str = None
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
                    }
                )
            except KeyError:
                continue

        return separate_data

    def __separete_all_data(self, api_response: List[Dict]) -> List[Dict]:

        countries = self.__get_countries.all_countries()["data"]

        separete_all_data = {}
        separate_data = []

        for country in countries:

            if country.name == "WORLD":
                continue

            for index, day in enumerate(api_response[country.name]):

                try:
                    separate_data.append(
                        {
                            "id": index + 1,
                            "date": day["date"],
                            "new_cases": day["new_cases"],
                            "country": country.name,
                        }
                    )
                except KeyError:
                    continue

            separete_all_data[country.name] = separate_data[:]
            separate_data.clear()

        return separete_all_data
