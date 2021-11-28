"""Predicts Covid19"""
from datetime import timedelta
from math import sqrt
import pandas as pd
from numpy import mean
from sklearn.metrics import mean_squared_error
from ..database.fetch_data import DadosCovid
from .. import config

dc = DadosCovid(config.search_url, "BRA")
data = dc.read_data_from_brazil()


class AnalizadorDeCovid():
    """Realizar a analise dos dados coletados do Covid-19"""

    def __init__(self, data_base, days):
        self.data_base = data_base
        self.days = days

    def adicionar_dias_ao_data_frame(self):
        """Adiciona os dias a serem previstos"""
        current_day = self.data_base[-1][0]
        count = 0
        while count < self.days:
            current_day += timedelta(days = 1)
            self.data_base.append((current_day, -1))
            count += 1

    def vidente_carlinhos(self):
        """
        Realiza a previsão de casos de covid no proximo dia,
        com base na média de casos de dois dias atrás.
        """
        self.adicionar_dias_ao_data_frame()
        data_frame = pd.DataFrame(self.data_base)

        X = data_frame.values
        window = 2
        history = [X[i][1] for i in range(window)]
        test = [X[i][1] for i in range(window, len(X))]
        predicoes = []

        for index, value in enumerate(test):

            length = len(history)
            valor_predito = mean([history[i] for i in range(length - window, length)])

            if value < 0:
                test[index] = valor_predito
                valor_real = test[index]
            valor_real = test[index]
            predicoes.append(valor_predito)
            history.append(valor_real)

            print(f'Dia: {X[index][0]}:\
                    Valor predito: {valor_predito:.0f},\
                    Valor real:{valor_real:.0f}')

        rmse = sqrt(mean_squared_error(test, predicoes))
        print(f'Metrica de RMSE: {rmse}')


dados = AnalizadorDeCovid(data, 12)
dados.vidente_carlinhos()
