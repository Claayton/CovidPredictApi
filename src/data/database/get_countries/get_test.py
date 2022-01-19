"""Diretório de tests para a classe GetCountry"""
from faker import Faker
from src.infra.tests import CountryRepoSpy
from .get import GetCountry

faker = Faker()


def test_by_name():
    """Testando o método by_name"""

    country_repo = CountryRepoSpy()
    get_country = GetCountry(country_repo)

    attributes = {"name": faker.name()}
    response = get_country.by_name(attributes["name"])

    assert country_repo.get_countries_params["name"] == attributes["name"]

    assert response["success"] is True
    assert response["data"]


def test_by_id():
    """Testando o método by_id"""

    country_repo = CountryRepoSpy()
    get_country = GetCountry(country_repo)

    attributes = {"country_id": faker.random_number(digits=2)}
    response = get_country.by_id(attributes["country_id"])

    assert country_repo.get_countries_params["country_id"] == attributes["country_id"]

    assert response["success"] is True
    assert response["data"]


def test_all_countries():
    """Testando o método all_countries"""

    country_repo = CountryRepoSpy()
    get_country = GetCountry(country_repo)

    response = get_country.all_countries()

    assert country_repo.get_countries_params["name"] is None

    assert response["success"] is True
    assert response["data"]


def test_by_name_fail():
    """Testando o erro no método by_name"""

    country_repo = CountryRepoSpy()
    get_country = GetCountry(country_repo)

    attributes = {"name": faker.random_number(digits=5)}
    response = get_country.by_name(attributes["name"])

    assert country_repo.get_countries_params == {}

    assert response["success"] is False
    assert response["data"] is None
