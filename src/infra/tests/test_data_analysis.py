"""Testes relacionados a analise dos dados coletados"""
from datetime import date
from src.analyzer.data_analysis import CovidAnalyzer

def test_if_add_days_to_data_frame_is_working():
    """
    Teste para garantir que o sistema consegue adicionar os dias a serem previstos.
    """
    data = [
        (date(2021, 1, 1),69074),
        (date(2021, 1, 2), 57837),
        (date(2021, 1, 3), 52383)
    ]
    today = date.today()
    ac = CovidAnalyzer(data, 0)
    response = ac.add_days_to_data_frame()
    assert response == today

# def test_if_predict_covid_evolution_is_working():
#     """
#     Teste para garantir que a função de analise esta funcionando da forma correta
#     """
#     data = [
#         (date(2021, 1, 1),7000),
#         (date(2021, 1, 2), 6000),
#         (date(2021, 1, 3), 5000),
#         (date(2021, 1, 4),4000),
#         (date(2021, 1, 5), 3000),
#         (date(2021, 1, 6), 2000),
#         (date(2021, 1, 7),1000),
#     ]
#     ac = CovidAnalyzer(data, 7)
#     response = ac.predict_covid_evolution()
#     assert 'predito' in response[0]
#     assert int(response[0]['predito']) == 262
