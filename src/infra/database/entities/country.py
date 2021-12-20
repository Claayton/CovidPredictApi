"Criação de banco de dados e tabelas"
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.database.config import Base


class Country(Base):
    """
    Tabela de dados sobre o covid-19 no brasil nos ultimos 600 dias aproximadamente.
    """

    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    daily = relationship("world_days")

    def __repr__(self):
        return f"Date <{self.date}>"
