"tables"

from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app/database.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


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

def create_database():
    """cria a tabela no banco de dados"""
    Base.metadata.create_all(engine)
