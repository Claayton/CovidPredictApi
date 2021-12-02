"Criação de banco de dados e tabelas"

import os.path
from time import sleep
from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app/database/datacovid.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def create_database_if_not_exist(file):
    """
    Verifica se o arquivo datacovid.db existe,
    em caso negativo, cria o arquivo já com as tabelas prontas.
    """
    if os.path.isfile(file):
        print(f'\033[35m{"=" * 75}\033[m')
        print(f'\033[35m{"Arquivo de dados encontrado...":^75}\033[m')
        sleep(2)
    else:
        print(f'\033[35m{"=" * 75}\033[m')
        print(f'\033[35m{"Arquivo de dados não encontrado, criando arquivo...":^75}\033[m')
        sleep(2)
        Base.metadata.create_all(engine)

def delete_arquivo_if_exist(file):
    """
    Verifica se o aqruivo datacovid.db existe, em caso positivo, deleta o arquivo.
    """
    if os.path.isfile(file):
        os.remove(file)


class CovidBrazil(Base):
    """
    Tabela de dados sobre o covid-19 no brasil nos ultimos 600 dias aproximadamente.
    """
    __tablename__ = 'covid_brazil'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    new_cases = Column(Integer)

    def __repr__(self):
        return f"Date <{self.date}>"


class CovidWorld(Base):
    """
    Tabela de dados sobre o covid-19 no mundo nos ultimos 600 dias aproximadamente.
    """
    __tablename__ = 'covid_world'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    new_cases = Column(Integer)

    def __repr__(self):
        return f"Date <{self.date}>"
