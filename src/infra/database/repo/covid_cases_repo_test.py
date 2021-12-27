"""Diretório de testes para a classe CovidCasesRepo"""
from datetime import date
from faker import Faker
from src.infra.database.config import DataBaseConnectionHandler
from .covid_cases_repo import CovidCasesRepo

faker = Faker()
covid_cases_repo = CovidCasesRepo()
data_base_connection_handler = DataBaseConnectionHandler()


def test_insert_data():
    """Testando o método insert_data"""

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


def test_update_cases():
    """Testando o método update_cases"""

    cases_id = faker.random_number(digits=5)
    data_date = faker.date()
    new_cases = faker.random_number(digits=5)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO covid_cases (id, date, new_cases, country_id)\
          VALUES ('{cases_id}', '{data_date}', '{new_cases}', '{1}');"
    )

    update_covid_case = covid_cases_repo.update_cases(cases_id, 123)

    query_update_covid_case = engine.execute(
        f"SELECT * FROM covid_cases WHERE id='{update_covid_case.id}';"
    ).fetchone()

    assert update_covid_case.id == query_update_covid_case.id
    assert update_covid_case.id == cases_id
    assert update_covid_case.date == date.fromisoformat(data_date)
    assert update_covid_case.country_id == 1
    assert update_covid_case.new_cases == query_update_covid_case.new_cases
    assert update_covid_case.new_cases != new_cases

    engine.execute(f"DELETE FROM covid_cases WHERE id='{cases_id}';")


def test_get_data_by_country():
    """Testando o método get_data_by_country"""

    cases_id = faker.random_number(digits=5)
    data_date = faker.date()
    new_cases = faker.random_number(digits=5)
    country = "BRA"

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO covid_cases (id, date, new_cases, country_id)\
          VALUES ('{cases_id}', '{data_date}', '{new_cases}', '{1}');"
    )

    query_covid_cases = covid_cases_repo.get_data_by_country(country=country)

    assert isinstance(query_covid_cases, list)
    assert isinstance(query_covid_cases[0][0], int)
    assert isinstance(query_covid_cases[0][1], date)
    assert isinstance(query_covid_cases[0][2], int)
