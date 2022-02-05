"""Testes para a classe GetCountry"""
from faker import Faker
from src.infra.tests import CountryRepoSpy
from .get import GetCountry

faker = Faker()


def test_by_name():
    """Testando o método by_name"""

    countries_repo = CountryRepoSpy()
    get_countries = GetCountry(countries_repo)

    attribute = {"name": faker.name()}
    response = get_countries.by_name(attribute["name"])

    # Testando a entrada:
    # Testando se o attributo enviado para countries_repo é o mesmo enviado para o método.
    assert countries_repo.get_countries_params["name"] == attribute["name"]

    # Testando a saída:
    assert response["success"] is True
    assert response["data"]


def test_by_name_error():
    """
    Testando o erro no método by_name.
    Enviando um número inteiro para o attributo name, que deveria ser uma string.
    """

    countries_repo = CountryRepoSpy()
    get_countries = GetCountry(countries_repo)

    attributes = {"name": faker.random_number(digits=5)}
    response = get_countries.by_name(attributes["name"])

    # Testando a entrada:
    # Testando se o attributo enviado para countries_repo é igual a {}, pois o vlaor é inválido.
    assert countries_repo.get_countries_params == {}

    # Testando a saída:
    assert response["success"] is False
    assert response["data"] is None


def test_by_id():
    """Testando o método by_id"""

    countries_repo = CountryRepoSpy()
    get_countries = GetCountry(countries_repo)

    attribute = {"country_id": faker.random_number(digits=2)}
    response = get_countries.by_id(attribute["country_id"])

    # Testando a entrada:
    # Testando se o attributo enviado para countries_repo é o mesmo enviado para o método.
    assert countries_repo.get_countries_params["country_id"] == attribute["country_id"]

    # Testando a saída:
    assert response["success"] is True
    assert response["data"]


def test_by_id_error():
    """
    Testando o erro no método by_id.
    Enviando uma string para o attributo country_id, que deveria ser um número inteiro.
    """

    countries_repo = CountryRepoSpy()
    get_countries = GetCountry(countries_repo)

    attribute = {"country_id": faker.name()}
    response = get_countries.by_id(attribute["country_id"])

    # Testando a entrada:
    # Testando se o attributo enviado para countries_repo é igual a {}, pois o vlaor é inválido.
    assert countries_repo.get_countries_params == {}

    # Testando a saída:
    assert response["success"] is False
    assert response["data"] is None


def test_all_countries():
    """Testando o método all_countries"""

    countries_repo = CountryRepoSpy()
    get_countries = GetCountry(countries_repo)

    response = get_countries.all_countries()

    # Testando a entrada:
    # Testando se o attributo enviado para countries_repo é o mesmo enviado para o método.
    assert countries_repo.get_countries_params["name"] is None

    #Testando a saída:
    assert response["success"] is True
    assert response["data"]
