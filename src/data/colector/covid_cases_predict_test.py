"""Testes para a classe CovidCasesPredict"""
from src.data.colector import CovidCasesPredict
from src.data.tests import GetCovidCasesSpy


def test_covid_evolution_predict():
    """
    Testando o método covid_evolution_predict.
    """

    get_covid_cases = GetCovidCasesSpy(None)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)

    attributes = {"country": "BRA", "days": 4}

    response = covid_cases_predict.covid_evolution_predict(
        attributes["country"], attributes["days"]
    )

    get_covid_cases_attributes = get_covid_cases.by_country_params["country"]

    # Testando a entreada:
    # Testando se os atributos enviados para get_covid_cases são os mesmos enviados para o método.
    assert get_covid_cases_attributes == attributes["country"]

    # Testando a saída:
    assert response["success"] is True
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)
    assert "country" in response["data"][0]
    assert "new_cases_real" in response["data"][0]


def test_covid_evolution_predict_error_1():
    """
    Testando o erro no método covid_evolution_predict.
    Enviando um número inteiro no attributo country, que deveria ser uma string.
    """

    get_covid_cases = GetCovidCasesSpy(None)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)

    attributes = {"country": 5, "days": 4}

    response = covid_cases_predict.covid_evolution_predict(
        attributes["country"], attributes["days"]
    )

    get_covid_cases_attributes = get_covid_cases.by_country_params

    # Testando a entreada:
    # Testando se os atributos enviados para get_covid_cases é igual a {},
    # pois os attributos enviado são inválidos.
    assert get_covid_cases_attributes == {}

    # Testando a saída:
    assert response["success"] is False
    assert "error" in response["data"]


def test_covid_evolution_predict_error_2():
    """
    Testando o erro no método covid_evolution_predict.
    Enviando uma string no attributo days, que deveria ser um número inteiro.
    """

    get_covid_cases = GetCovidCasesSpy(None)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)

    attributes = {"country": "BRA", "days": "cinquenta"}

    response = covid_cases_predict.covid_evolution_predict(
        attributes["country"], attributes["days"]
    )

    get_covid_cases_attributes = get_covid_cases.by_country_params

    # Testando a entreada:
    # Testando se os atributos enviados para get_covid_cases é igual a {},
    # pois os attributos enviado são inválidos.
    assert get_covid_cases_attributes == {}

    # Testando a saída:
    assert response["success"] is False
    assert "error" in response["data"]
