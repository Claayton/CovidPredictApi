"""Testes para a classe CovidCasesPredictController"""
from faker import Faker
from src.data.colector import CovidCasesPredict
from src.infra.tests import CovidCasesRepoSpy
from src.data.tests import GetCovidCasesSpy
from src.presenters.helpers import HttpRequest
from . import CovidCasesPredictController

faker = Faker()


def test_handler_full_query():
    """Testando o método handler"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCasesSpy(covid_cases_repo)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)
    covid_cases_predict_controller = CovidCasesPredictController(covid_cases_predict)

    http_request = HttpRequest(
        query={"country": faker.name(), "days": faker.random_number(digits=1)}
    )

    response = covid_cases_predict_controller.handler(http_request)

    assert response.status_code == 200
    assert response.body["success"] is True
    assert "date" in response.body["data"][0]
    assert "new_cases_real" in response.body["data"][0]
    assert "predicted_evolution" in response.body["data"][0]
