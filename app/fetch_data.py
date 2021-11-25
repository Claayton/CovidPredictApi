"""Script de pesquisa e cadastro de dados na API"""
from datetime import date
import requests
from .tables import CovidBrazil, session

search_url = "https://covid.ourworldindata.org/data/owid-covid-data.json"

def fetch_data_by_country(url, country):
    """
    Buscar dos dados da COVID-19 por cada país.
    :param country: País no qual deve ser buscados os dados
    :return: Uma lista de cada dia desde 26-02-2020,
    separados por id, data e número de novos casos registrados no país.
    """
    response = requests.get(url).json()
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

def register_data_from_brazil():
    """registra os dados do brasil no banco de dados"""
    brasilian_data = fetch_data_by_country(search_url, "BRA")

    for data in brasilian_data:
        new_day = CovidBrazil(
            date=date.fromisoformat(data["date"]),
            new_cases=int(data["new_cases"])
        )
        session.add(new_day)
        print(new_day)
    session.commit()

def read_data_from_brazil():
    """faz a leitura dos dados no banco de dados"""
    querry = session.query(CovidBrazil.date, CovidBrazil.new_cases).all()
    return querry


# register_data_from_brazil()
read_data_from_brazil()

# def fetch_world_data(countries):
#     """
#     Buscar dos dados mundiais da COVID-19.
#     :param countries: Lista de países no qual deve ser buscados os dados.
#     :return: Uma lista de cada dia desde 26-02-2020,
#     separados por id, data e número de novos casos registrados no mundo.
#     """
#     world_data_per_day = []

#     for country in countries:
#         country_data = fetch_data_by_country(country)
#         if not world_data_per_day:
#             world_data_per_day = country_data[:]
#             country_data.clear()
#         else:
#             for index, item in enumerate(world_data_per_day):
#                 if item["date"] == country_data[index]["date"]:
#                     item["new_cases"] += country_data[index]["new_cases"]
#     return world_data_per_day

# print(fetch_world_data(all_countries)[0])
