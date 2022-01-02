"Instância da tabela Country e seus métodos"
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.database.config import Base


class Country(Base):
    """
    Tabela contendo todos os países do mundo que foram coletados os dados do covid19.
    """

    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    covid_cases = relationship("CovidCases", back_populates="countries")

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"Country <{self.name}>"

    def __eq__(self, other):
        if self.id == other.id and self.name == other.name:
            return True
        return False
