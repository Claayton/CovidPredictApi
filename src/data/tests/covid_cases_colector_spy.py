"""Classe Spy para CovidCasesColector"""
from typing import List, Type, Dict
from src.errors import HttpErrors
from src.domain.usecases import (
    CovidCasesColectorInterface,
    GetCountriesInterface as GetCountries,
)
from src.infra.tests import mock_data_covid


class CovidCasesColectorSpy(CovidCasesColectorInterface):
    """Spy para CovidCasesColector"""

    def __init__(self, get_countries: Type[GetCountries]) -> None:
        self.__get_countries = get_countries
        self.covid_cases_country_attributes = {}
        self.covid_cases_world_attributes = {}

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
            http_error = HttpErrors.error_422()

            return {"success": False, "data": http_error}

        self.covid_cases_country_attributes["country"] = country

        api_response = mock_data_covid()["BRA"]

        country_data_response = self.__separete_data(api_response, days, country)

        return {"success": True, "data": country_data_response}

    def covid_cases_world(self, days: int) -> Dict[bool, List[Dict]]:
        """
        Realiza o tratamento dos dados do covid do mundo inteiro recebidos do consumer.
        :param days: A quantidade de dias futuros que devem ser previstos.
        :return: Os dados do covid19 ja tratados e com uma previsão para os próximos dias.
        """

        countries = self.__get_countries.all_countries()["data"]

        self.covid_cases_world_attributes["countries"] = countries

        api_response = mock_data_covid()

        countries_data = []

        for country in countries:

            country_data = api_response[country.name]
            each_country = self.__separete_data(country_data, days, country)

            countries_data.append(each_country)

            world_data_response = self.__world_data_sum(countries_data, days)

        return {"success": True, "data": world_data_response}

    @classmethod
    def __world_data_sum(cls, countries_data: List[List], days: int) -> List[Dict]:

        world_data_response = []

        for country in countries_data:
            for index, day in enumerate(country):

                date = day["date"]
                new_cases = day["new_cases"]

                if date == day["date"]:
                    new_cases += new_cases

                world_data_response.append(
                    {
                        "id": index,
                        "date": date,
                        "new_cases": new_cases,
                        "country": "WORLD",
                        "days": days,
                    }
                )

        return world_data_response

    @classmethod
    def __separete_data(
        cls, data_days: List[Dict], days: int, country: str = None
    ) -> List[Dict]:

        separate_data = []

        for index, day in enumerate(data_days):

            try:
                separate_data.append(
                    {
                        "id": index,
                        "date": day["date"],
                        "new_cases": day["new_cases"],
                        "country": country,
                        "days": days,
                    }
                )
            except KeyError:
                continue

        return separate_data