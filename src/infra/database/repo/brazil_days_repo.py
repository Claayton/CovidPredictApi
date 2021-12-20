"""Administração dos dados"""
from typing import Type
from datetime import datetime
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import CovidBrazil


class BrasilDayRepo:
    """A simple repository"""

    @classmethod
    def insert_brazil_data(cls, date: Type[datetime], new_cases: int) -> None:
        """
        Registra os dados do brasil relacionados ao COvid-19 no banco de dados.
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                new_data = CovidBrazil(
                    date=date.fromisoformat("1997-08-01"), new_cases="123"
                )
                data_base.session.add(new_data)
                data_base.session.commit()
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()
