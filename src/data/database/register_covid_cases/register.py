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

        data_covid = self.__covid_cases_colector.covid_cases_colector()["data"]
        countries = self.__get_countries.all_countries()["data"]

        country_response = []
        response = {}

        for country in countries:

            print(f"{country.id} : {country.name}")
            if country.name == "WORLD":
                continue

            try:

                for day in data_covid[country.name]:
                    insertion = self.__covid_cases_repo.insert_data(
                        data_date=day["date"],
                        new_cases=day["new_cases"],
                        country_id=country.id,
                    )
                    country_response.append(
                        {
                            "id": insertion.id,
                            "date": str(insertion.date).split()[0],
                            "new_cases": insertion.new_cases,
                            "country_id": insertion.country_id,
                        }
                    )

            except Exception as error:
                raise error

            response[country.name] = country_response[:]
            country_response.clear()

        return {"success": True, "data": response}
