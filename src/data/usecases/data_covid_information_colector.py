"""Caso de uso para DataCovidInformation"""
from typing import List, Type, Dict

# from datetime import date, datetime
import pandas as pd
from numpy import mean
from src.domain.usecases.data_covid_information_colector import (
    DataCovidInformationColectorInterface,
)
from src.data.interfaces.data_covid_consumer import DataCovidConsumerInterface


class DataCovidInformationColector(DataCovidInformationColectorInterface):
    """DataCovidInformationColector usecase"""

    def __init__(self, api_consumer: Type[DataCovidConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_country(self, country: str, time: int) -> Dict:
        country_information = self.__search_country(country)

        predicted_evolution = self.__calculate_predict_covid_evolution(
            country_information, time
        )

        formated_response = self.__format_response(predicted_evolution, country)
        return formated_response

    def __search_country(self, country: str) -> Dict:
        api_response = self.__api_consumer.get_data_covid_information(country)

        return api_response.response

    @classmethod
    def __calculate_predict_covid_evolution(
        cls, data_base: List[Dict], time: int
    ) -> List[Dict]:
        """
        Realiza a previsão de casos de covid nos proximos dias,
        com base na média de casos dos últimos 7 dias.
        :return: Uma lista com dados de previsão para cada dia,
        baseado na quantidade de dias escolhido a partir da data atual.
        """
        # self.add_days_to_data_frame(time)
        print(time)
        data_frame = pd.DataFrame(data_base)

        data_values = data_frame.values
        window = 3

        history = [data_values[i][2] for i in range(window)]
        test = [data_values[i][2] for i in range(window, len(data_values))]
        predicted = []
        predicted_evolution = []
        difference = 0

        for index, value in enumerate(test):

            length = len(history)
            average_of_previous_days = mean(
                [history[i] for i in range(length - window, length)]
            )

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

            # if datetime.strptime(data_values[index][1], "%Y-%m-%d") >= datetime.today():
            predicted_evolution.append(
                {
                    "id": data_values[index][1],
                    "date": data_values[index][0],
                    "new_cases_real": real_value,
                    "predicted_evolution": average_of_previous_days,
                }
            )
        return predicted_evolution

    @classmethod
    def __format_response(
        cls, predicted_evolution: List[Dict], country: str
    ) -> List[Dict]:

        result = []

        for day in predicted_evolution:
            result.append(
                {
                    "id": day["id"],
                    "date": day["date"],
                    "new_cases_real": day["new_cases_real"],
                    "predicted_evolution": day["predicted_evolution"],
                }
            )
        return {"country": country, "data": result}
