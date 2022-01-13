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


def test_handler_erro_422():
    """Testando o erro 422 (query inválida/query insuficiente) no método handler"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCasesSpy(covid_cases_repo)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)
    covid_cases_predict_controller = CovidCasesPredictController(covid_cases_predict)

    http_request1 = HttpRequest(query={"country": faker.random_number(digits=1)})
    http_request2 = HttpRequest(query={"days": faker.name()})
    http_request3 = HttpRequest(query={"country": faker.name()})
    http_request4 = HttpRequest(query={"days": faker.random_number(digits=1)})

    response1 = covid_cases_predict_controller.handler(http_request1)
    response2 = covid_cases_predict_controller.handler(http_request2)
    response3 = covid_cases_predict_controller.handler(http_request3)
    response4 = covid_cases_predict_controller.handler(http_request4)

    assert response1.status_code == 422
    assert response2.status_code == 422
    assert response3.status_code == 422
    assert response4.status_code == 422

    assert "error" in response1.body
    assert "error" in response2.body
    assert "error" in response3.body
    assert "error" in response4.body


def test_handler_erro_400():
    """Testando o erro 400 (BadRequest) no método handler"""

    covid_cases_repo = CovidCasesRepoSpy()
    get_covid_cases = GetCovidCasesSpy(covid_cases_repo)
    covid_cases_predict = CovidCasesPredict(get_covid_cases)
    covid_cases_predict_controller = CovidCasesPredictController(covid_cases_predict)

    http_request = HttpRequest()

    response = covid_cases_predict_controller.handler(http_request)

    assert response.status_code == 400
    assert "error" in response.body
