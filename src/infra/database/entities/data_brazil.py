"Criação de banco de dados e tabelas"
from sqlalchemy import Column, Integer, Date
from src.infra.database.config import Base


class CovidBrazil(Base):
    """
    Tabela de dados sobre o covid-19 no brasil nos ultimos 600 dias aproximadamente.
    """

    __tablename__ = "covid_brazil"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    new_cases = Column(Integer)

    def __repr__(self):
        return f"Date <{self.date}>"
