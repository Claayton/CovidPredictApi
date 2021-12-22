"Criação de banco de dados e tabelas"
from sqlalchemy import Column, Integer, Date
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database.config import Base


class CovidCases(Base):
    """
    Tabela de dados sobre o covid-19 no mundo nos ultimos 600 dias aproximadamente.
    """

    __tablename__ = "covid_cases"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    new_cases = Column(Integer)

    country_id = Column(Integer, ForeignKey("countries.id"))
    countries = relationship("Country", back_populates="covid_cases")

    def __init__(self, date: str, new_cases: int, country_id: int) -> None:
        self.date = date
        self.new_cases = new_cases
        self.country_id = country_id

    def __repr__(self):
        return f"Date <{self.date}>"
