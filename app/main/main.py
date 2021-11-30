"""Módulo principal do programa"""

from sqlalchemy.exc import OperationalError
from app import config
from app.interface.app_interface import Interface
from app.database.fetch_data import DadosCovid
from app.analyzer.data_analise import AnalizadorDeCovid

def run():
    interface = Interface()
    dc = DadosCovid(config.search_url, "BRA")

    choice = interface.main_menu()
    if choice == 0:
        try:
            data = dc.read_data_from_brazil()
            if not data:
                raise ValueError()
        except (OperationalError, ValueError):
            dc.register_data_from_brazil()
            data = dc.read_data_from_brazil()
            print(data)
        days = interface.read_data_menu('Brasil')
        ac = AnalizadorDeCovid(data, days)
        ac.adicionar_dias_ao_data_frame()
        ac.vidente_carlinhos()
    else:
        try:
            data = dc.read_data_from_world()
            if not data:
                raise  ValueError()
        except (OperationalError, ValueError):
            dc.register_data_from_world()
            data = dc.read_data_from_world()
        days = interface.read_data_menu('Mundo')
        ac = AnalizadorDeCovid(data, days)
        ac.adicionar_dias_ao_data_frame()
        ac.vidente_carlinhos()
