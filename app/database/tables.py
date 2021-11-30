"tables"

import os.path
from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

file = 'app/database/datacovid.db'
engine = create_engine(f'sqlite:///{file}', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def create_database_if_not_exist(file='app/database/datacovid.db'):
    if os.path.isfile(file):
        print('\033[35mBanco de dados já existe\033[m')
    else:
        print(f'\033[35mFile {file} does not exist!, creating...\033[m')
        Base.metadata.create_all(engine)


class CovidBrazil(Base):
    """Dados sobre o covid no brasil nos ultimos 600 dias."""
    __tablename__ = 'covid_brazil'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    new_cases = Column(Integer)

    def __repr__(self):
        return f"Date <{self.date}>"


class CovidWorld(Base):
    """Dados sobre o covid no mundo nos ultimos 600 dias."""
    __tablename__ = 'covid_world'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    new_cases = Column(Integer)

    def __repr__(self):
        return f"Date <{self.date}>"
