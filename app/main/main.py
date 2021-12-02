"""Módulo principal do programa"""

from sqlalchemy.exc import OperationalError
from app import config
from app.interface.app_interface import Interface
from app.database.fetch_data import DadosCovid
from app.analyzer.data_analysis import CovidAnalyzer
from app.database.tables import delete_arquivo_if_exist

def run():
    """Rodar diretamente o programa"""

    interface = Interface()

    while True:
        while True:
            choice = interface.main_menu()
            if choice == 0:
                delete_arquivo_if_exist('app/database/datacovid.db')
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
        for day in result:
            print(f'Dia: {day["index"]}:\
                    Previsão: {day["predito"]:.2f}')
        again = interface.again()
        if again[0] in 'Nn':
            interface.farewall()
            break
