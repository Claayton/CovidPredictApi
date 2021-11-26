"tables"

from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app/database/datacovid.db', echo=True)

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

    @classmethod
    def find_by_date(cls, current_session, date):
        return current_session.query(cls).filter_by(date=date).all()

def create_database_if_not_exist():
    """cria a tabela no banco de dados"""
    file = 'app/database/datacovid.db'
    try:
        a = open(file, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        print(f'File {file} does not exist!, creating...')
        Base.metadata.create_all(engine)
        return False
