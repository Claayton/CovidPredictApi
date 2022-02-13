"""Criação dos bancos de dados de teste"""
from src.config import CONNECTION_STRING, CONNECTION_STRING_TESTS
from src.infra.database.entities import *  # pylint: disable=W0401, W0614
from . import DataBaseConnectionHandler, Base


def create_database():
    """Criação do banco de dados de desenvolvimento"""

    db_connection = DataBaseConnectionHandler(CONNECTION_STRING)
    engine = db_connection.get_engine()
    base = Base.metadata.create_all(engine)

    return base


def create_tests_database():
    """Criação do banco de dados de testes"""

    db_connection_tests = DataBaseConnectionHandler(CONNECTION_STRING_TESTS)
    engine_tests = db_connection_tests.get_engine()
    base = Base.metadata.create_all(engine_tests)

    return base
