"""Diretório de manipulação de dados"""
from typing import List, Tuple
from collections import namedtuple
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import Country


class CountryRepo:
    """Manipulação de dados da tabela Country"""

    @classmethod
    def insert_country(cls, name: str) -> Country:
        """
        Realiza a inserção de um novo país na tabela Country.
        :param name: Nome ou abreviação do nome do país.
        :return: Uma tupla nomeada com os todos os dados do novo país cadastrado.
        """

        insert_data = namedtuple("Country", "id name")

        with DataBaseConnectionHandler() as data_base:
            try:
                new_country = Country(name=name)
                data_base.session.add(new_country)
                data_base.session.commit()
                return insert_data(id=new_country.id, name=new_country.name)
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    @classmethod
    def get_countries(cls) -> List[Tuple]:
        """
        Realiza a busca de todos os países cadastrados.
        :return: Uma lista com tuplas de todos países cadastrados.
        """

        try:
            with DataBaseConnectionHandler() as data_base:
                query_data = data_base.session.query(Country.name).all()
            return query_data
        except:
            data_base.session.rollback()
            raise
        finally:
            data_base.session.close()
