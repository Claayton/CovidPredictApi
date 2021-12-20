"Criação de banco de dados e tabelas"
from sqlalchemy import Column, Integer, Date
from sqlalchemy.sql.schema import ForeignKey
from src.infra.database.config import Base


class WorldDay(Base):
    """
    Tabela de dados sobre o covid-19 no mundo nos ultimos 600 dias aproximadamente.
    """

    __tablename__ = "world_days"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    new_cases = Column(Integer)

    country_id = Column(Integer, ForeignKey("countries"))

    def __repr__(self):
        return f"Date <{self.date}>"
