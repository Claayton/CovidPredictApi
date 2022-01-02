"""Diretório do caso de uso RegisterCovidCases"""
from typing import Type, Dict
from src.domain.usecases import RegisterCovidCasesInterface
from src.data.interfaces import CovidCasesRepoInterface as CovidCasesRepo
from src.data.get_countries import GetCountry
from src.domain.models import CovidCases


class RegisterCovidCases(RegisterCovidCasesInterface):
    """Classe para definir o caso de uso: RegisterCovidCases"""

    def __init__(
        self, covid_cases_repo: Type[CovidCasesRepo], get_countries: Type[GetCountry]
    ) -> None:
        self.covid_cases_repo = covid_cases_repo
        self.get_countries = get_countries

    def register(
        self, date: str, new_cases: int, country: str
    ) -> Dict[bool, CovidCases]:
        """
        Registro de dados de casos de covid19 no banco de dados.
        :param date: Data de coleta dos dados.
        :param new_cases: Quantidade de novos casos registrados.
        :param country: Abreviação do nome do país de referência.
        :return: Um dicionário com as informações do processo.
        """

        response = None

        validate_entry = (
            isinstance(date, str)
            and isinstance(new_cases, int)
            and isinstance(country, str)
        )
        country_id = self.get_countries.by_name(name=country)["data"][0].id
        checker = (validate_entry) and (country_id is not None)

        if checker:
            response = self.covid_cases_repo.insert_data(
                data_date=date, new_cases=new_cases, country_id=country_id
            )

        return {"success": checker, "data": response}
