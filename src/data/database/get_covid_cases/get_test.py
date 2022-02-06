"""Diretório de tests para a classe GetCovidCases"""
from faker import Faker
from src.infra.tests import CovidCasesRepoSpy
from .get import GetCovidCases

faker = Faker()


def test_by_country():
    """Testando o método by_country"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attribute = {"country": faker.name()}
    response = get_covid_cases.by_country(country=attribute["country"])

    # Testando a entrada:
    # Testando se o attributo enviado para covid_cases_repo é o mesmo enviado para o método.
    assert covid_cases_repo.get_covid_cases_params["country"] == attribute["country"]

    # Testando a saída:
    assert response["success"] is True
    assert response["data"]


def test_by_country_error():
    """
    Testando o erro no método by_country.
    Enviando um número inteiro para o attributo country, que deveria ser uma string.
    """

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attribute = {"country": faker.random_number(digits=4)}
    response = get_covid_cases.by_country(country=attribute["country"])

    # Testando a entrada:
    # Testando se o attributo enviado para covid_cases_repo é  igual a {}, pois é um valor inválido.
    assert covid_cases_repo.get_covid_cases_params == {}

    # Testando a saída:
    assert response["success"] is False
    assert response["data"] is None


def test_by_date():
    """Testando o método by_date"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attribute = {"data_date": faker.date()}
    response = get_covid_cases.by_date(data_date=attribute["data_date"])

    # Testando a entrada:
    # Testando se o attributo enviado para covid_cases_repo é o mesmo enviado para o método.
    assert (
        covid_cases_repo.get_covid_cases_params["data_date"] == attribute["data_date"]
    )

    # Testando a saída:
    assert response["success"] is True
    assert response["data"]


def test_by_date_error():
    """
    Testando o método by_date.
    Enviando um número inteiro para o attributo by_date, que deveria ser uma string.
    """

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attribute = {"data_date": faker.random_number(digits=1)}
    response = get_covid_cases.by_date(data_date=attribute["data_date"])

    # Testando a entrada:
    # Testando se o attributo enviado para covid_cases_repo é  igual a {}, pois é um valor inválido.
    assert covid_cases_repo.get_covid_cases_params == {}

    # Testando a saída:
    assert response["success"] is False
    assert response["data"] is None


def test_by_country_and_by_date():
    """Testando o erro no método by_country_and_by_date"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attributes = {"country": faker.name(), "data_date": faker.date()}

    response = get_covid_cases.by_country_and_by_date(
        country=attributes["country"], data_date=attributes["data_date"]
    )

    # Testando a entrada:
    # Testando se os attributos enviados para covid_cases_repo são os mesmos enviados para o método.
    assert covid_cases_repo.get_covid_cases_params["country"] == attributes["country"]
    assert (
        covid_cases_repo.get_covid_cases_params["data_date"] == attributes["data_date"]
    )

    # Testando a saída:
    assert response["success"] is True
    assert response["data"]


def test_by_country_and_by_date_fail():
    """
    Testando o erro no método by_country_and_by_date.
    Enviando números inteiros para os attributos country e by_date, que deveriam ser strings.
    """

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCases(covid_cases_repo)

    attributes = {
        "country": faker.random_number(digits=4),
        "data_date": faker.random_number(digits=1),
    }
    response = get_covid_cases.by_country_and_by_date(
        country=attributes["country"], data_date=attributes["data_date"]
    )

    # Testando a entrada:
    # Testando se o attributo enviado para covid_cases_repo é  igual a {}, pois é um valor inválido.
    assert covid_cases_repo.get_covid_cases_params == {}

    # Testando a saída:
    assert response["success"] is False
    assert response["data"] is None
