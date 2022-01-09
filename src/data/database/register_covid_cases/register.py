"""Diretório do caso de uso RegisterCovidCases"""
from typing import List, Type, Dict
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
    ) -> None:
        self.__covid_cases_colector = covid_cases_colector
        self.__covid_cases_repo = covid_cases_repo
        self.__get_countries = get_countries

    def register_covid_cases_by_country(
        self, country: str
    ) -> Dict[bool, List[CovidCases]]:
        """
        Registro de dados de casos de covid19 no banco de dados.
        :param country: Abreviação do nome do país de referência.
        :return: Um dicionário com as informações do processo.
        """

        full_response = []
        response = None

        validate_entry = isinstance(country, str)
        if validate_entry:
            country_id = self.__get_countries.by_name(name=country)["data"][0].id

        checker = (validate_entry) and (country_id is not None)
        if checker:

            data_covid = self.__covid_cases_colector.covid_cases_country(
                country=country
            )

            for day in data_covid:

                response = self.__covid_cases_repo.insert_data(
                    data_date=day["date"],
                    new_cases=day["new_cases"],
                    country_id=country_id,
                )
                full_response.append(response)

        return {"success": checker, "data": full_response}
