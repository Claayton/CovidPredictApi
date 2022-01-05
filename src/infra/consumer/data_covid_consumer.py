"""Diretório para a classe DataCovidConsumer"""
from json.decoder import JSONDecodeError
from typing import Dict, List, Tuple, Type
from collections import namedtuple
from requests import Request, Session
from src.errors import HttpRequestError, HttpErrors
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
        self.get_all_data_covid_response = namedtuple(
            "GET_Dados_covid", "status_code request response"
        )
        self.get_data_covid_by_country_response = namedtuple(
            "GET_Dados_covid_Info", "status_code request response"
        )

    def get_countries(self) -> Tuple[int, Type[Request], List]:
        """
        Realiza a requisição para a API de dados do covid.
        :return: Uma tupla nomeada com os atributos:
            status_code: O status da resposta,
            request: A requisição http enviada,
            response: Uma lista com todos os países encontrados na resposta da API.
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

    def get_all_data_covid(self) -> Tuple[int, Type[Request], Dict]:
        """
        Realiza a requisição para a API de dados do covid.
        :return: Uma tupla nomeada com os atributos:
            status_code: O status da resposta,
            request: A requisição http enviada,
            response: Um dicionário contendo todos os países, e seus dados sobre o covid.
        """

        request = Request(method="GET", url=self.url)
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code
        response_json = response.json()
        response_data = {}

        try:
            for country in response_json:
                response_data[country] = response_json[country]["data"]
        except TypeError:
            raise HttpRequestError(message=response, status_code=status_code)

        if (status_code < 200) or (status_code > 299):
            raise HttpRequestError(message=response, status_code=status_code)
        return self.get_all_data_covid_response(
            status_code=status_code, request=request, response=response_data
        )

    def get_data_covid_by_country(
        self, country: str
    ) -> Tuple[int, Type[Request], List[Dict]]:
        """
        Realiza a requisição para a API de dados do covid.
        :param country: O país do qual deve ser retornado os dados
        :return: Uma tupla nomeada com os atributos:
            status_code: O status da resposta,
            request: A requisição http enviada,
            response: Uma lista com dicionários,
                contendo dados sobre o covid por dia no país requisitado.
        """

        request = Request(method="GET", url=self.url)
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code

        try:
            data = response.json()[country]["data"]
        except (KeyError, JSONDecodeError):
            http_error = HttpErrors.error_422()
            status_code = http_error["status_code"]
            data = http_error["body"]

        if (status_code < 200) or (status_code > 299):
            raise HttpRequestError(message=response, status_code=status_code)
        return self.get_data_covid_by_country_response(
            status_code=status_code,
            request=request,
            response=data,
        )

    @classmethod
    def __send_http_request(cls, request_prepared: Type[Request]) -> any:
        """
        Prepara a seção e envia a requisição http.
        :param request_prepared: Objeto de requisição com todos os parâmetros.
        :return: A resposta da requisição http.
        """

        http_session = Session()
        response = http_session.send(request_prepared)

        return response
