"Instância da tabela CovidCases e seus métodos"
from sqlalchemy import Column, Integer, Date
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database.config import Base


class CovidCases(Base):
    """
    Tabela de dados do covid19 por país, com dados de todo o mundo nos ultimos 600 dias.
    """

    __tablename__ = "covid_cases"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    new_cases = Column(Integer)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)

    countries = relationship("Country", back_populates="covid_cases")

    def __init__(self, date: str, new_cases: int, country_id: int) -> None:
        self.date = date
        self.new_cases = new_cases
        self.country_id = country_id

    def __repr__(self):
        return f"Date <{self.date}>"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.date == other.date
            and self.new_cases == other.new_cases
        ):
            return True
        return False
