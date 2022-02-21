"""Classe Spy para CovidCasesColector"""
from typing import List, Type, Dict
from src.errors import HttpUnprocessableEntityError
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

    def covid_cases_colector(self, country: str = None) -> Dict[bool, List[Dict]]:
        """
        Realiza o tratamento dos dados do covid por país recebidos do consumer.
        :param country: O país de referência que deverá ser tratado os dados.
        :param days: A quantidade de dias futuros que devem ser previstos.
        :return: Os dados do covid19 ja tratados e com uma previsão para os próximos dias.
        """

        country_exist = self.__get_countries.by_name(name=country)

        if not country_exist["success"]:
            http_error = HttpUnprocessableEntityError(message="Invalid Country!")

            return {"success": False, "data": http_error}

        self.covid_cases_country_attributes["country"] = country

        api_response = mock_data_covid()["BRA"]

        country_data_response = self.__separete_data(api_response, country)

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
