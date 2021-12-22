"""Administração dos dados"""
from typing import List, Tuple
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import Country


class CountryRepo:
    """A simple repository"""

    @classmethod
    def insert_country(cls, name: str) -> None:
        """
        Registra os dados do brasil relacionados ao COvid-19 no banco de dados.
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                new_country = Country(name=name)
                data_base.session.add(new_country)
                data_base.session.commit()
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    @classmethod
    def get_countries(cls) -> List[Tuple]:
        """Selecionar todos os paises"""

        try:
            with DataBaseConnectionHandler() as data_base:
                query_data = data_base.session.query(Country.name).all()
            return query_data
        except:
            data_base.session.rollback()
            raise
        finally:
            data_base.session.close()
