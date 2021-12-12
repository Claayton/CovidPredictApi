"""Script de analise de e previsão do Covid-19"""
from datetime import timedelta, date
import pandas as pd
from numpy import mean


class CovidAnalyzer():
    """Realizar a analise dos dados coletados do Covid-19"""

    def __init__(self, data_base, days):
        self.data_base = data_base
        self.days = days

    def add_days_to_data_frame(self):
        """
        Adiciona o número de dias que serão previstos à base de dados real.
        :return: A data do proximo dia adicionado (para fins de teste).
        """
        current_day = self.data_base[-1][0]
        today = date.today()
        count = 0

        # Completa os dias até a data atual com previsões caso os dados da API estejam incompletos
        while current_day < today:
            current_day += timedelta(days=1)
            self.data_base.append((current_day, -666))

        # Completa os dias somando o numero de dias escolhido para prever
        # +6 pq o sistema precisa dessa folga para realizar a previsão
        while count < self.days + 6:
            current_day += timedelta(days=1)
            self.data_base.append((current_day, -666))
            count += 1
        return self.data_base[-7][0]

    def predict_covid_evolution(self):
        """
        Realiza a previsão de casos de covid nos proximos dias,
        com base na média de casos dos últimos 7 dias.
        :return: Uma lista com dados de previsão para cada dia,
        baseado na quantidade de dias escolhido a partir da data atual.
        """
        self.add_days_to_data_frame()
        data_frame = pd.DataFrame(self.data_base)

        X = data_frame.values
        window = 7

        history = [X[i][1] for i in range(window)]
        test = [X[i][1] for i in range(window, len(X))]
        predicted = []
        result = []
        difference = 0

        for index, value in enumerate(test):

            length = len(history)
            average_of_previous_days = mean([history[i] for i in range(length - window, length)])
            
            # Adiciona 10% ou subtrai 15% ao suposto valor real de casos previstos,
            # Dependendo da diferença entre o ultimo e penúltimo dos 7 dias anteriores.
            if difference > 0:
                hope = average_of_previous_days + (average_of_previous_days * 10 / 100)
            else:
                hope = average_of_previous_days - (average_of_previous_days * 15 / 100)

            real_value = value
            if value == -666:
                real_value = hope

            previous_days = [history[i] for i in range(length - window, length)]
            difference = previous_days[-1] - previous_days[-2]


            predicted.append(average_of_previous_days)
            history.append(real_value)


            if X[index][0] >= date.today():
                result.append({
                    'index': X[index][0],
                    'predito': average_of_previous_days,
                    'real': real_value
                })
        return result
