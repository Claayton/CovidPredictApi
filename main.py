"""Script de execução do programa"""

from app import config
from app.interface.app_interface import Interface
from app.database.fetch_data import DadosCovid
from app.database.tables import create_database_if_not_exist

interface = Interface()
dc = DadosCovid(config.search_url, "BRA")

create_database_if_not_exist()
choice = interface.main_menu()
if choice == 0:
    data = dc.read_data_from_brazil()
    if not data:
        dc.register_data_from_brazil()
        data = dc.read_data_from_brazil()
else:
    data = dc.read_data_from_world()
    if not data:
        dc.register_data_from_world()
        data = dc.read_data_from_world()
        print('nao tem nada aqui fio')
    print(data)
