"""Diretório do caso de uso RegisterCovidCases"""
from typing import Type, Dict
from src.data.database.get_countries import GetCountry
from src.domain.models import CovidCases
from src.data.interfaces import CovidCasesRepoInterface as CovidCasesRepo
from src.domain.usecases import (
    RegisterCovidCasesInterface,
    CovidCasesColectorInterface as CovidCasesColector,
)


class RegisterCovidCases(RegisterCovidCasesInterface):
    """Classe para definir o caso de uso: RegisterCovidCases"""

    def __init__(
        self,
        covid_cases_colector: Type[CovidCasesColector],
        covid_cases_repo: Type[CovidCasesRepo],
        get_countries: Type[GetCountry],
    ) -> Dict[bool, CovidCases]:
        self.__covid_cases_colector = covid_cases_colector
        self.__covid_cases_repo = covid_cases_repo
        self.__get_countries = get_countries

    def register_covid_cases(self) -> Dict[bool, CovidCases]:
        """
        Registro de dados de todos casos de covid19 vindos da API, no banco de dados.
        :return: Um dicionário com as informações do processo.
        """

        countries = self.__get_countries.all_countries()["data"]
        response = []

        for country in countries:

            try:

                data_covid = self.__covid_cases_colector.covid_cases_country(
                    country=country.name
                )

                for day in data_covid["data"]:

                    insertion = self.__covid_cases_repo.insert_data(
                        data_date=day["date"],
                        new_cases=day["new_cases"],
                        country_id=country.id,
                    )
                    response.append(insertion)

            except Exception as error:
                raise error

        return {"success": True, "data": response}
