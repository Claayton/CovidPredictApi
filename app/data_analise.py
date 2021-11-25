"""Predicts Covid19"""
from math import sqrt
import pandas as pd
from numpy import mean
from sklearn.metrics import mean_squared_error
from fetch_data import read_data_from_brazil
from datetime import datetime, timedelta

data = read_data_from_brazil()

def adicionar_dias_ao_data_frame(df, dias):
    current_day = df[-1][0]
    for c in range(0, dias):
        current_day += timedelta(days = 1)
        df.append((current_day, 0))

adicionar_dias_ao_data_frame(data, 5)

data_frame = pd.DataFrame(data)

print(data_frame)

def vidente_carlinhos():
    """
    Realiza a previsão de casos de covid no proximo dia,
    com base na média de casos de dois dias atrás.
    """
    X = data_frame.values
    window = 2
    history = [X[i][1] for i in range(window)]
    test = [X[i][1] for i in range(window, len(X))]
    predicoes = []

    for t in range(len(test)):

        length = len(history)
        
        valor_predito = mean([history[i] for i in range(length - window, length)])
        valor_real = test[t]
        predicoes.append(valor_predito)
        history.append(valor_real)
        print(f'Dia: {X[t][0]}: Valor predito: {valor_predito:.2f}, Valor real: {valor_real:.2f}')

    rmse = sqrt(mean_squared_error(test, predicoes))  
    print(f'Metrica de RMSE: {rmse}')

vidente_carlinhos()
