"""Script de pesquisa e registro de dados na API"""
from datetime import date
import requests
from src.database.countries_list import all_countries
from src.database.tables import CovidBrazil, CovidWorld, session, create_database_if_not_exist
from src.interface.app_interface import Interface

interface = Interface()


class DataCovidConsumer:
    """Realiza o tratamento dos dados do covid no brasil"""

    def __init__(self, country: str):
        create_database_if_not_exist('app/database/datacovid.db')
        self.country = country

    @classmethod
    def get_data_covid(self, ) -> any:
        """ Busca dados na Api"""

        response = requests.get('https://covid.ourworldindata.org/data/owid-covid-data.json/')
        return response.json()

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

    def separates_data_from_the_world(self, ):
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
        interface.collecting_data()

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
        interface.collecting_data()

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
