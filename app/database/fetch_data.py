"""Script de pesquisa e cadastro de dados na API"""
from datetime import date
import requests
from app.database.tables import CovidBrazil, CovidWorld, session
from app.database.countries_list import all_countries


class DadosCovid():
    """Realiza o tratamento dos dados do covid no brasil"""

    def __init__(self, url, country):
        self.url = url
        self.country = country

    def fetch_data_by_country(self, country):
        """
        Buscar dos dados da COVID-19 por cada país.
        :param country: País no qual deve ser buscados os dados
        :return: Uma lista de cada dia desde 26-02-2020,
        separados por id, data e número de novos casos registrados no país.
        """
        response = requests.get(self.url).json()
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
                pass
        return country_data_per_day

    def register_data_from_brazil(self):
        """Registra os dados do brasil relacionados ao COvid-19 no banco de dados"""
        brazil_data = self.fetch_data_by_country("BRA")

        for data in brazil_data:
            new_day = CovidBrazil(
                date=date.fromisoformat(data["date"]),
                new_cases=int(data["new_cases"])
            )
            session.add(new_day)
            print(new_day)
        session.commit()

    def register_data_from_world(self):
        """Registra os dados do mundo inteiro relacionados ao Covid-19 no banco de dados"""

        for country in all_countries:
            world_data = self.fetch_data_by_country(country)

            query = session.query(CovidWorld.new_cases).first()
            if not query:
                for data in world_data:
                    new_day = CovidWorld(
                    date=date.fromisoformat(data["date"]),
                    new_cases=int(data["new_cases"])
                    )
                session.add(new_day)
            else:
                for data in world_data:
                    query = CovidWorld.find_by_date(session, data["date"])
                    print(f'\033[35m{data["date"]}\033[m')
                    print(f'\033[32m{query}\033[m')
                    query.new_cases = self + int(data["new_cases"])
                    session.commit()

    def read_data_from_brazil(self):
        """faz a leitura dos dados no banco de dados"""
        query = session.query(CovidBrazil.date, CovidBrazil.new_cases).all()
        return query

    def read_data_from_world(self):
        """faz a leitura dos dados no banco de dados"""
        query = session.query(CovidWorld.date, CovidWorld.new_cases).all()
        return query
