"""Testes para a classe CountryRepo"""
from faker import Faker
from src.infra.database.config import DataBaseConnectionHandler
from src import config
from .countries_repo import CountryRepo

faker = Faker()
country_repo = CountryRepo(config.CONNECTION_STRING_TESTS)
data_base_connection_handler = DataBaseConnectionHandler(config.CONNECTION_STRING_TESTS)


def test_insert_country():
    """Teste para inserção de novos países no banco de dados"""

    name = faker.word().upper()
    engine = data_base_connection_handler.get_engine()

    new_country = country_repo.insert_country(name)
    query_country = engine.execute(
        f"SELECT * FROM countries WHERE name='{new_country.name}';"
    ).fetchone()

    # Testando se as informações enviadas pelo método  podem ser encontradas no db.
    assert new_country.id == query_country.id
    assert new_country.name == query_country.name

    engine.execute(f"DELETE FROM countries WHERE id='{new_country.id}';")


def test_get_countries_by_name():
    """
    Teste para a busca de países no banco de dados.
    Utilizando o parâmetro name.
    """

    country_id = faker.random_number(digits=10)
    name = faker.name()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO countries (id, name) VALUES ('{country_id}', '{name}');"
    )
    engine.execute(f"SELECT * FROM countries WHERE name='{name}';")

    query_country = country_repo.get_countries(name=name)

    # Testando se as informações enviadas pelo método  podem ser encontradas no db.
    assert isinstance(query_country, list)
    assert query_country[-1].name == name
    assert query_country[-1].id == country_id

    engine.execute(f"DELETE FROM countries WHERE id='{country_id}';")


def test_get_countries_by_country_id():
    """
    Teste para a busca de países no banco de dados.
    Utilizando o parâmetro country_id.
    """

    country_id = faker.random_number(digits=10)
    name = faker.name()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO countries (id, name) VALUES ('{country_id}', '{name}');"
    )
    engine.execute(f"SELECT * FROM countries WHERE name='{name}';")

    query_country = country_repo.get_countries(country_id=country_id)

    # Testando se as informações enviadas pelo método  podem ser encontradas no db.
    assert isinstance(query_country, list)
    assert query_country[-1].name == name
    assert query_country[-1].id == country_id

    engine.execute(f"DELETE FROM countries WHERE id='{country_id}';")


def test_get_countries_by_name_and_by_country_id():
    """
    Teste para a busca de países no banco de dados.
    Utilizando o parâmetro country_id.
    """

    country_id = faker.random_number(digits=10)
    name = faker.name()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO countries (id, name) VALUES ('{country_id}', '{name}');"
    )
    engine.execute(f"SELECT * FROM countries WHERE name='{name}';")

    query_country = country_repo.get_countries(name=name, country_id=country_id)

    # Testando se as informações enviadas pelo método  podem ser encontradas no db.
    assert isinstance(query_country, list)
    assert query_country[-1].name == name
    assert query_country[-1].id == country_id

    engine.execute(f"DELETE FROM countries WHERE id='{country_id}';")


def test_get_countries_without_name_and_without_country_id():
    """
    Teste para a busca de países no banco de dados.
    Utilizando o parâmetro country_id.
    """

    country_id = faker.random_number(digits=10)
    name = faker.name()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO countries (id, name) VALUES ('{country_id}', '{name}');"
    )
    engine.execute(f"SELECT * FROM countries WHERE name='{name}';")

    query_country = country_repo.get_countries()

    # Testando se as informações enviadas pelo método  podem ser encontradas no db.
    assert isinstance(query_country, list)
    assert query_country[-1] is not None

    engine.execute(f"DELETE FROM countries WHERE id='{country_id}';")
