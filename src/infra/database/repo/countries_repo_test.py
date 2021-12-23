"""Testes para a classe CountryRepo"""
from faker import Faker
from src.infra.database.config import DataBaseConnectionHandler
from .countries_repo import CountryRepo

faker = Faker()
country_repo = CountryRepo()
data_base_connection_handler = DataBaseConnectionHandler()


def test_insert_country():
    """Teste para inserção de novos países no banco de dados"""

    name = faker.word().upper()
    engine = data_base_connection_handler.get_engine()

    new_country = country_repo.insert_country(name)
    query_country = engine.execute(
        f"SELECT * FROM countries WHERE id='{new_country.id}';"
    ).fetchone()

    engine.execute(f"DELETE FROM countries WHERE id='{new_country.id}';")

    assert new_country.id == query_country.id
    assert new_country.name == query_country.name


def test_get_countries():
    """Teste ára a busca de países no banco de dados"""

    country_id = faker.random_number(digits=10)
    name = faker.name()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO countries (id, name) VALUES ('{country_id}', '{name}');"
    )
    engine.execute("SELECT * FROM countries;")

    query_country = country_repo.get_countries()

    assert isinstance(query_country, list)
    assert query_country[-1].id == country_id

    engine.execute(f"DELETE FROM countries WHERE id='{country_id}';")
