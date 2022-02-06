"""Diretório de manipulação de dados"""
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from src.data.interfaces import CountryRepoInterface
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import Country as CountryModel
from src.domain.models import Country
from src import config


class CountryRepo(CountryRepoInterface):
    """Manipulação de dados da tabela Country"""

    def __init__(self, connection_string: str = config.CONNECTION_STRING) -> None:
        self.__connection_string = connection_string

    def insert_country(self, name: str) -> Country:
        """
        Realiza a inserção de um novo país na tabela Country.
        :param name: Nome ou abreviação do nome do país.
        :return: Uma tupla nomeada com os todos os dados do novo país cadastrado.
        """

        insert_data = None

        with DataBaseConnectionHandler(self.__connection_string) as data_base:
            try:
                new_country = CountryModel(name=name)
                data_base.session.add(new_country)
                data_base.session.flush()

                insert_data = Country(id=new_country.id, name=new_country.name)

            except IntegrityError:
                data_base.session.rollback()
                existing = (
                    data_base.session.query(CountryModel).filter_by(name=name).one()
                )
                if not existing:
                    raise
            else:
                data_base.session.commit()
                insert_data = Country(id=new_country.id, name=new_country.name)
            finally:
                data_base.session.close()

        return insert_data

    def get_countries(self, name: str = None, country_id: int = None) -> List[Country]:
        """
        Realiza a busca dos países cadastrados no banco de dados.
        Os dados podem ser especificados pelo name ou pelo country_id.
        Caso nenhum dos parâmetros sejam passados, o sistema retornará todos os dados cadastrados.
        :param name: Abreviação do nome do país.
        :param country_id: Id do país ja cadastrado no banco de dados
        :return: Uma lista com os dados de países requeridos.
        """

        try:
            query_data = None

            if name:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:
                    data = (
                        data_base.session.query(CountryModel).filter_by(name=name).one()
                    )
                    query_data = [data]

            elif country_id:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:
                    data = (
                        data_base.session.query(CountryModel)
                        .filter_by(id=country_id)
                        .one()
                    )
                    query_data = [data]

            else:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:
                    data = data_base.session.query(CountryModel).all()
                    query_data = data

            return query_data

        except NoResultFound:
            return None
        except Exception as error:
            data_base.session.rollback()
            raise error
        finally:
            try:
                data_base.session.close()
            except UnboundLocalError:
                pass
