"""Diretório para a classe DataCovidConsumer"""
from typing import Dict, List, Tuple, Type
from collections import namedtuple
from requests import Request, Session
from src.errors import HttpRequestError
from src.data.interfaces.data_covid_consumer import DataCovidConsumerInterface


class DataCovidConsumer(DataCovidConsumerInterface):
    """
    Classe responsável pelo consumo da API de dados do covid utilizando requisições http.
    """

    def __init__(self, url: str) -> None:
        self.url = url
        self.get_countries_response = namedtuple(
            "GET_Countries", "status_code request response"
        )
        self.get_covid_cases_response = namedtuple(
            "GET_Dados_covid", "status_code request response"
        )
        self.get_covid_cases_by_country_response = namedtuple(
            "GET_Dados_covid_Info", "status_code request response"
        )

    def get_countries(self) -> Tuple[int, Type[Request], List]:
        """
        Realiza a requisição para a API de dados covid.
        :return: Uma lista com todos os países encontrados na resposta da API.
        """

        request = Request(method="GET", url=self.url)
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code
        data = response.json()

        countries = []

        for country in data:
            countries.append(country)

        if (status_code < 200) or (status_code > 299):
            raise HttpRequestError(message=response, status_code=status_code)
        return self.get_countries_response(
            status_code=status_code, request=request, response=countries
        )

    def get_data_covid(self) -> Tuple[int, Type[Request], Dict]:
        """
        Realiza a requisição para a API de dados do covid.
        :return: Uma tupla com os atributos: (status_code, request, response).
        """

        request = Request(method="GET", url=self.url)
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code

        if (status_code < 200) or (status_code > 299):
            raise HttpRequestError(message=response, status_code=status_code)
        return self.get_covid_cases_response(
            status_code=status_code, request=request, response=response.json()
        )

    def get_data_covid_information(
        self, country: str
    ) -> Tuple[int, Type[Request], Dict]:
        """
        Realiza a requisição para a API de dados do covid,
        retornando apenas os dados de um único país.
        :param country: O país do qual deve ser retornado os dados
        :return: Uma tupla com seus atributos (status_code, request, response).
        """

        request = Request(
            method="GET",
            url=f"{self.url}",
        )
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code

        if 200 > status_code > 299:
            raise HttpRequestError(message=response, status_code=status_code)
        return self.get_covid_cases_by_country_response(
            status_code=status_code,
            request=request,
            response=response.json()[country]["data"],
        )

    @classmethod
    def __send_http_request(cls, request_prepared: Type[Request]) -> any:
        """
        Prepara a seção e envia a requisição http
        :param request_prepared: Objeto de requisição com todos os parâmetros.
        :return: A resposta da requisição http.
        """

        http_session = Session()
        response = http_session.send(request_prepared)
        return response

    # def register_data_from_brazil(self):
    #     """
    #     Registra os dados do brasil relacionados ao Covid-19,
    #     no banco de dados.
    #     """

    #     brazil_data = self.separates_data_from_a_country("BRA")

    #     for data in brazil_data:
    #         new_day = CovidBrazil(
    #             date=date.fromisoformat(data["date"]),
    #             new_cases=int(data["new_cases"])
    #         )
    #         session.add(new_day)
    #     session.commit()

    # def register_data_from_world(self):
    #     """
    #     Registra os dados do mundo inteiro relacionados ao Covid-19
    #     no banco de dados.
    #     """

    #     world_data_list = {}
    #     world_data_by_country = self.separates_data_from_the_world()
    #     world_data_list = world_data_by_country[0]

    #     for country in world_data_by_country:
    #         for day in country:

    #             current_date = day["date"]
    #             current_new_cases = day["new_cases"]

    #             for day_world_list in world_data_list:
    #                 if current_date == day_world_list["date"]:
    #                     day_world_list["new_cases"] += current_new_cases

    #     for data in world_data_list:
    #         new_day = CovidWorld(
    #             date=date.fromisoformat(data["date"]),
    #             new_cases=int(data["new_cases"])
    #         )
    #         session.add(new_day)
    #     session.commit()

    # def read_data_from_brazil(self):
    #     """
    #     Realiza a leitura dos dados do Brasil no banco de dados.
    #     """
    #     query = session.query(CovidBrazil.date, CovidBrazil.new_cases).all()
    #     return query

    # def read_data_from_world(self):
    #     """
    #     Realiza a leitura dos dados do mundo no banco de dados.
    #     """
    #     query = session.query(CovidWorld.date, CovidWorld.new_cases).all()
    #     return query
