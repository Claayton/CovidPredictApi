"""Script de pesquisa e registro de dados na API"""
from datetime import date
from typing import Dict, Tuple, Type
from collections import namedtuple
import requests
from requests import Request
from src.database.countries_list import all_countries
from src.database.tables import CovidBrazil, CovidWorld, session, create_database_if_not_exist
from src.errors import HttpRequestError
from src.data.interfaces.data_covid_consumer import DataCovidConsumerInterface


class DataCovidConsumer(DataCovidConsumerInterface):
    """
    Classe responsável pelo consumo da API de dados do covid utilizando requisições http.
    """

    def __init__(self, url: str) -> None:
        self.get_data_covid_response = namedtuple(
            'GET_Dados_covid',
            'status_code request response'
        )
        self.url = url
        # create_database_if_not_exist('app/database/datacovid.db')

    def get_data_covid(self) -> Tuple[int, Type[Request], Dict]:
        """
        Realiza a requisição para a API de dados do covid.
        :return: Uma tupla com os atributos: (status_code, request, response).
        """

        request = requests.Request(
            method='GET',
            url=self.url,
        )
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code

        if (status_code >= 200) and (status_code <= 299):
            return self.get_data_covid_response(
                status_code=status_code,
                request=request,
                response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()['details'],
                status_code=status_code
            )

    @classmethod
    def __send_http_request(cls, request_prepared: Type[Request]) -> any:
        """
        Prepara a seção e envia a requisição http
        :param request_prepared: Objeto de requisição com todos os parâmetros.
        :return: A resposta da requisição http.
        """
        http_session = requests.Session()
        response = http_session.send(request_prepared)
        return response

    def separates_data_from_a_country(self, country: str) -> list:
        """
        Buscar dos dados da COVID-19 por cada país.
        :param country: País no qual deve ser buscados os dados
        :return: Uma lista de cada dia desde 26-02-2020,
        separados por id, data e número de novos casos registrados no país.
        """
        response = self.get_data_covid()
        days = response[country]["data"]

        country_data_per_day = []
        data = {}

        for index, day in enumerate(days):
            try:
                data["id"] = index
                data["date"] = day["date"]
                data["new_cases"] = day["new_cases"]
                country_data_per_day.append(data.copy())
                data.clear()
            except KeyError:
                continue
        return country_data_per_day

    def separates_data_from_the_world(self):
        """
        Busca dados de todos os paises do mundo,
        Realiza a soma dos casos de cada dia em todos os países do mundo
        :return: Uma lista com os casos de cada dia no mundo.
        """
        world_data_by_country = []
        country_data_per_day = []
        data = {}

        response = self.get_data_covid()

        for country in all_countries:
            data_by_country = response[country]["data"]
            for index, day in enumerate(data_by_country):
                try:
                    data["id"] = index
                    data["date"] = day["date"]
                    data["new_cases"] = day["new_cases"]
                    country_data_per_day.append(data.copy())
                    data.clear()
                except KeyError:
                    continue
            world_data_by_country.append(country_data_per_day[:])
            country_data_per_day.clear()

        return world_data_by_country

    def register_data_from_brazil(self):
        """
        Registra os dados do brasil relacionados ao COvid-19 no banco de dados.
        """

        brazil_data = self.separates_data_from_a_country("BRA")

        for data in brazil_data:
            new_day = CovidBrazil(
                date=date.fromisoformat(data["date"]),
                new_cases=int(data["new_cases"])
            )
            session.add(new_day)
        session.commit()

    def register_data_from_world(self):
        """
        Registra os dados do mundo inteiro relacionados ao Covid-19 no banco de dados.
        """

        world_data_list = {}
        world_data_by_country = self.separates_data_from_the_world()
        world_data_list = world_data_by_country[0]

        for country in world_data_by_country:
            for day in country:

                current_date = day["date"]
                current_new_cases = day["new_cases"]

                for day_world_list in world_data_list:
                    if current_date == day_world_list["date"]:
                        day_world_list["new_cases"] += current_new_cases

        for data in world_data_list:
            new_day = CovidWorld(
                date=date.fromisoformat(data["date"]),
                new_cases=int(data["new_cases"])
            )
            session.add(new_day)
        session.commit()

    def read_data_from_brazil(self):
        """
        Realiza a leitura dos dados do Brasil no banco de dados.
        """
        query = session.query(CovidBrazil.date, CovidBrazil.new_cases).all()
        return query

    def read_data_from_world(self):
        """
        Realiza a leitura dos dados do mundo no banco de dados.
        """
        query = session.query(CovidWorld.date, CovidWorld.new_cases).all()
        return query
