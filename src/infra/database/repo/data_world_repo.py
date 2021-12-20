"""Administração dos dados"""
from datetime import date
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import CovidWorld


class WorldDayRepo:
    """A simple repository"""

    @classmethod
    def insert_data(cls):
        """something"""

        with DataBaseConnectionHandler() as data_base:
            try:
                new_data = CovidWorld(
                    date=date.fromisoformat("1997-08-01"), new_cases="123"
                )
                data_base.session.add(new_data)
                data_base.session.commit()
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()
