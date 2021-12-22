"""Administração dos dados"""
from datetime import date
from src.infra.database.config import DataBaseConnectionHandler
from src.infra.database.entities import CovidCases
from src.infra.database.entities.countries import Country


class CovidCasesRepo:
    """A simple repository"""

    def insert_data(self, data_date: str, new_cases: int, country: str) -> None:
        """Inserir novos dados na tabela CovidCases"""

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
        """Atualizar dados ja cadastrados no banco"""

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

    @classmethod
    def __find_country_id(cls, country: str) -> int:
        """Busca o id do pais pelo nome"""

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
