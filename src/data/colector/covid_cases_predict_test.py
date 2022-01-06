"""Testes para a classe CovidCasesPredict"""
from src.data.colector import CovidCasesPredict
from src.data.tests import GetCovidCasesSpy


def test_covid_evolution_predict():
    """
    Testando o método covid_evolution_predict.
    """

    get_covid_cases = GetCovidCasesSpy(None)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)

    country = "BRA"
    days = 4

    response = covid_cases_predict.covid_evolution_predict(country, days)

    assert get_covid_cases.by_country_params == {"country": country}
    assert isinstance(response, list)
    assert "country" in response[0]
    assert "new_cases_real" in response[0]
