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
