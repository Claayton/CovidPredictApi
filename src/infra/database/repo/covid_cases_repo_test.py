"""Diretório de testes para a classe CovidCasesRepo"""
from datetime import date
from faker import Faker
from src.infra.database.config import DataBaseConnectionHandler
from .covid_cases_repo import CovidCasesRepo

faker = Faker()
covid_cases_repo = CovidCasesRepo()
data_base_connection_handler = DataBaseConnectionHandler()


def test_insert_data():
    """Testando o metodo insert_data"""

    data_date = faker.date()
    new_cases = faker.random_number(digits=5)
    country = "BRA"

    new_covid_case = covid_cases_repo.insert_data(data_date, new_cases, country)
    engine = data_base_connection_handler.get_engine()
    query_covid_cases = engine.execute(
        f"SELECT * FROM covid_cases WHERE id='{new_covid_case.id}';"
    ).fetchone()

    assert new_covid_case.id == query_covid_cases.id
    assert new_covid_case.date == date.fromisoformat(query_covid_cases.date)
    assert new_covid_case.new_cases == query_covid_cases.new_cases
    assert new_covid_case.country_id == query_covid_cases.country_id

    engine.execute(f"DELETE FROM covid_cases WHERE id='{new_covid_case.id}';")
