"""Diretório de manipulação de dados"""
from typing import List
from src.data.interfaces import CountryRepoInterface
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import Country as CountryModel
from src.domain.models import Country


class CountryRepo(CountryRepoInterface):
    """Manipulação de dados da tabela Country"""

    @classmethod
    def insert_country(cls, name: str) -> Country:
        """
        Realiza a inserção de um novo país na tabela Country.
        :param name: Nome ou abreviação do nome do país.
        :return: Uma tupla nomeada com os todos os dados do novo país cadastrado.
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                new_country = CountryModel(name=name)
                data_base.session.add(new_country)
                data_base.session.commit()

                return Country(id=new_country.id, name=new_country.name)
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    @classmethod
    def get_countries(cls, name: str = None) -> List[Country]:
        """
        Realiza a busca dos países cadastrados no banco de dados.
        :param name: Abreviação do nome do país.
        :return: Uma lista com todos países cadastrados.
        """

        try:
            query_data = None

            if name:
                with DataBaseConnectionHandler() as data_base:
                    data = (
                        data_base.session.query(CountryModel).filter_by(name=name).one()
                    )
                    query_data = [data]
            else:

                with DataBaseConnectionHandler() as data_base:
                    data = data_base.session.query(CountryModel).all()
                    query_data = [data]
            return query_data

        except:
            data_base.session.rollback()
            raise
        finally:
            data_base.session.close()
