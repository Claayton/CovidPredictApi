"""Diretório de manipulação de dados"""
from datetime import date
from typing import Tuple, List
from src.data.interfaces import CovidCasesRepoInterface
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import CovidCases as CovidCasesModel
from src.domain.models import CovidCases
from src.infra.database.entities.countries import Country as CountryModel


class CovidCasesRepo(CovidCasesRepoInterface):
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
                    data_base.session.query(CountryModel)
                    .filter_by(name=country)
                    .first()
                )
                return country_id.id
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def insert_data(
        self, data_date: str, new_cases: int, country_id: int
    ) -> CovidCases:
        """
        Realiza a inserção de dados diários para a tabela CovidCases.
        :param data_date: Data de referência dos casos no formato string ('aaaa-mm-dd').
        :param new_cases: Novos casos de covid19 registrados.
        :param country: País de referência dos casos.
        :return: Uma tupla nomeada com os todos os novos dados cadastrado.
        """

        data_date = date.fromisoformat(data_date)

        with DataBaseConnectionHandler() as data_base:
            try:
                new_data = CovidCasesModel(
                    date=data_date, new_cases=new_cases, country_id=country_id
                )
                data_base.session.add(new_data)
                data_base.session.commit()

                return CovidCases(
                    id=new_data.id,
                    date=new_data.date,
                    new_cases=new_data.new_cases,
                    country_id=new_data.country_id,
                )
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    @classmethod
    def update_cases(cls, cases_id: int, new_cases: int) -> CovidCases:
        """
        Realiza a atualização dos dados ja cadastrados no banco na tabela CovidCases.
        :param id: ID de referência para realizar a atualização de dados.
        :param new_cases: Numero de novos casos de covid19 para atualização.
        :return: Uma tupla nomeada com os todos os novos dados cadastrado.
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                data_country = (
                    data_base.session.query(CovidCasesModel)
                    .filter_by(id=cases_id)
                    .first()
                )
                data_country.new_cases = new_cases
                data_base.session.commit()

                return CovidCases(
                    id=data_country.id,
                    date=data_country.date,
                    new_cases=data_country.new_cases,
                    country_id=data_country.country_id,
                )
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def get_data(
        self,
        country: str = None,
        data_date: str = None,
    ) -> List[Tuple]:
        """
        Realiza a busca de todos os dados de casos de covid, buscando por país.
        :param country: País de referência para a busca.
        :param data_date: Data de referência para a busca.
        :return: Uma lista com tuplas de todos os dados registrados do país.
        """

        try:

            query_data = None

            if country and not data_date:

                country_id = self.__find_country_id(country)

                with DataBaseConnectionHandler() as data_base:
                    data = (
                        data_base.session.query(CovidCasesModel)
                        .filter(CovidCasesModel.country_id == country_id)
                        .all()
                    )
                    query_data = [data]

            elif not country and data_date:

                data_date = date.fromisoformat(data_date)

                with DataBaseConnectionHandler() as data_base:
                    data = (
                        data_base.session.query(CovidCasesModel)
                        .filter(CovidCasesModel.date == data_date)
                        .all()
                    )
                    query_data = [data]

            elif country and data_date:

                country_id = self.__find_country_id(country)
                data_date = date.fromisoformat(data_date)

                with DataBaseConnectionHandler() as data_base:
                    data = (
                        data_base.session.query(CovidCasesModel)
                        .filter(
                            CovidCasesModel.country_id == country_id,
                            CovidCasesModel.date == data_date,
                        )
                        .all()
                    )
                    query_data = [data]

            return query_data

        except:
            data_base.session.rollback()
            raise
        finally:
            data_base.session.close()
