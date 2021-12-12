"""Módulo principal do programa"""

from sqlalchemy.exc import OperationalError
from src import config
from src.interface.app_interface import Interface
from src.database.fetch_data import DadosCovid
from src.analyzer.data_analysis import CovidAnalyzer
from src.database.tables import delete_arquivo_if_exist

def run():
    """Rodar diretamente o programa"""

    interface = Interface()

    while True:
        while True:
            choice = interface.main_menu()
            if choice == 0:
                delete_arquivo_if_exist('src/database/datacovid.db')
            else:
                break
        if choice == 777:
            interface.farewall()
            break
        dc = DadosCovid(config.search_url, "BRA")
        if choice == 1:
            try:
                data = dc.read_data_from_brazil()
                if not data:
                    raise ValueError()
            except (OperationalError, ValueError):
                dc.register_data_from_brazil()
                data = dc.read_data_from_brazil()
            days = interface.read_data_menu('Brasil')
            ac = CovidAnalyzer(data, days)
            result = ac.predict_covid_evolution()
        else:
            try:
                data = dc.read_data_from_world()
                if not data:
                    raise  ValueError()
            except (OperationalError, ValueError):
                dc.register_data_from_world()
                data = dc.read_data_from_world()
            days = interface.read_data_menu('Mundo')
            ac = CovidAnalyzer(data, days)
            result = ac.predict_covid_evolution()
        for index, day in enumerate(result):
            print(f'{day["index"]} -> {index + 1} -> {day["predito"]:.2f}')
        again = interface.again()
        if again[0] in 'Nn':
            interface.farewall()
            break
