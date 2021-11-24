"""main"""
import requests

def predict(days=1):
    """Função de teste temporária"""
    print("do stuff here")
    return days

def fetch_data_by_country(country):
    """
    Buscar dos dados da COVID-19 por cada país.
    :param country: País no qual deve ser buscados os dados
    :return: Uma lista de cada dia desde 26-02-2020,
    separados por id, data e número de novos casos registrados no país.
    """
    url = "https://covid.ourworldindata.org/data/owid-covid-data.json"
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

print(fetch_data_by_country("BRA")[0])
