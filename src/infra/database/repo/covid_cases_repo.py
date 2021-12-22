"""Diretório de manipulação de dados"""
from datetime import date
from typing import Tuple, List
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import CovidCases
from src.infra.database.entities.countries import Country


class CovidCasesRepo:
    """Manipulação de dados da tabela CovidCases"""

    @classmethod
    def __find_country_id(cls, country: str) -> int:
        """
        Encontrar o id de um país cadastrado no banco de dados.
        :param country: País de referência para a busca no banco.
        :return: O id do país desejado que esta cadastrado no banco de dados.
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                country_id = (
                    data_base.session.query(Country.id).filter_by(name=country).first()
                )
                return country_id
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def insert_data(self, data_date: str, new_cases: int, country: str) -> None:
        """
        Realiza a inserção de dados diários para a tabela CovidCases.
        :param data_date: Data de referência dos casos no formato string ('aaaa-mm-dd').
        :param new_cases: Novos casos de covid19 registrados.
        :param country: País de referência dos casos.
        """

        data_date = date.fromisoformat(data_date)
        country_id = self.__find_country_id(country)

        with DataBaseConnectionHandler() as data_base:
            try:
                new_data = CovidCases(data_date, new_cases, country_id[0])
                data_base.session.add(new_data)
                data_base.session.commit()
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def update_data(self, data_date: str, new_cases: int, country: str) -> None:
        """
        Realiza a atualização dos dados ja cadastrados no banco na tabela CovidCases.
        :param data_date: Data de referência dos casos no formato string ('aaaa-mm-dd').
        :param new_cases: Novos casos de covid19 registrados.
        :param country: País de referência dos casos.
        """

        data_date = date.fromisoformat(data_date)
        country_id = self.__find_country_id(country)

        with DataBaseConnectionHandler() as data_base:
            try:
                data_country = (
                    data_base.session.query(CovidCases)
                    .filter(
                        (CovidCases.country_id == country_id[0]),
                        (CovidCases.date == data_date),
                    )
                    .first()
                )
                data_country.date = data_date
                data_country.new_cases = new_cases
                data_country.country_id = country_id[0]
                data_base.session.commit()
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def get_data_by_country(self, country: str) -> List[Tuple]:
        """
        Realiza a busca de todos os dados de casos de covid, buscando por país.
        :param country: País de referência para a busca.
        :return: Uma lista com tuplas de todos os dados registrados do país.
        """

        country_id = self.__find_country_id(country)

        try:
            with DataBaseConnectionHandler() as data_base:
                query_data = (
                    data_base.session.query(
                        CovidCases.id, CovidCases.date, CovidCases.new_cases
                    )
                    .filter(CovidCases.country_id == country_id[0])
                    .all()
                )
            return query_data
        except:
            data_base.session.rollback()
            raise
        finally:
            data_base.session.close()
