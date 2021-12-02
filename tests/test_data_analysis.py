"""Testes relacionados a analise dos dados coletados"""
from datetime import date
from app.analyzer.data_analysis import CovidAnalyzer

def test_if_adicionar_dias_ao_data_frame_is_working():
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

def test_if_vidente_carlinhos_is_working():
    """
    Teste para garantir que a função de analise esta funcionando da forma correta
    """
    data = [
        (date(2021, 1, 1),69074),
        (date(2021, 1, 2), 57837),
        (date(2021, 1, 3), 52383),
        (date(2021, 1, 4),69074),
        (date(2021, 1, 5), 57837),
        (date(2021, 1, 6), 52383),
        (date(2021, 1, 7),69074),
    ]
    ac = CovidAnalyzer(data, 7)
    response = ac.predict_covid_evolution()[0]['predito']
    assert int(response) == 6052
