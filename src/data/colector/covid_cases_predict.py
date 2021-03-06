"""Caso de uso para CovidCasePredict"""
from typing import Type, Dict, List
from datetime import datetime, timedelta
import pandas as pd
from numpy import mean
from src.domain.usecases import (
    CovidCasesPredictInterface,
    GetCovidCasesInterface as GetCovidCases,
)


class CovidCasesPredict(CovidCasesPredictInterface):
    """Caso de uso para Previsão de casos de covid19"""

    def __init__(
        self,
        get_covid_cases: Type[GetCovidCases],
    ) -> None:
        self.__get_covid_cases = get_covid_cases

    def covid_evolution_predict(
        self, country: str, days: int
    ) -> Dict[bool, List[Dict]]:
        """
        Realiza a previsão de casos de covid nos proximos dias,
        com base na média de casos dos últimos 3 dias.
        :param country: País de referência para a previsão, (WORLD para dados mundiais).
        :param days: Dias no futuro que deve ser realizada a previsão.
        :return: Uma lista com dados de previsão para cada dia,
        baseado na quantidade de dias escolhido a partir da data atual.
        """

        if not isinstance(country, str) or not isinstance(days, int):
            return {
                "success": False,
                "data": {
                    "error": "Country value must be an integer, and days must be a string"
                },
            }

        covid_data = self.__format_data_covid(country, days)

        data_frame = pd.DataFrame(covid_data)

        data_values = data_frame.values
        window = 3

        history = [data_values[i][2] for i in range(window)]
        test = [data_values[i][2] for i in range(window, len(data_values))]
        predicted = []
        predicted_evolution = []
        difference = 0

        for index, value in enumerate(test):

            if index >= window:

                length = len(history)
                average_of_previous_days = mean(
                    [history[i] for i in range(length - window, length)]
                )

                # Adiciona 10% ou subtrai 15% ao suposto valor real de casos previstos,
                # Dependendo da diferença entre o ultimo e penúltimo dos 3 dias anteriores.
                if difference > 0:
                    hope = average_of_previous_days + (
                        average_of_previous_days * 10 / 100
                    )
                else:
                    hope = average_of_previous_days - (
                        average_of_previous_days * 15 / 100
                    )

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
                        "id": data_values[index][0],
                        "date": data_values[index][1],
                        "new_cases_real": real_value,
                        "predicted_evolution": average_of_previous_days,
                        "country": country,
                    }
                )

        return {"success": True, "data": predicted_evolution}

    def __format_data_covid(self, country: str, days: int) -> Dict:

        covid_data = self.__get_covid_cases.by_country(country)

        response = []

        for data in covid_data["data"]:

            response.append(
                {
                    "id": data.id,
                    "date": str(data.date).split()[0],
                    "new_cases": data.new_cases,
                    "country_id": data.country_id,
                }
            )

        covid_data_plus_days = self.__add_days_to_data_frame(response, days)

        return covid_data_plus_days

    @classmethod
    def __add_days_to_data_frame(cls, data_covid: List[Dict], days: int) -> List[Dict]:
        """
        Adiciona o número de dias que serão previstos à base de dados real.
        :return: A nova base de dados, atualizada com os novos dias.
        """

        unformat_current_day = str(data_covid[-1]["date"]).split()[0]
        current_day = datetime.strptime(unformat_current_day, "%Y-%m-%d")
        today = datetime.today()
        count = 1
        index = 0

        # Completa os dias até a data atual + 3 (window de previsão),
        # Com previsões caso os dados da API estejam incompletos.
        while current_day < today + timedelta(days=3):
            current_day += timedelta(days=1)
            data_covid.append(
                {
                    "id": index,
                    "date": str(current_day).split()[0],
                    "new_cases": -666,
                    "country_id": data_covid[0]["country_id"],
                }
            )
            index += 1

        # Completa os dias somando o numero de dias escolhido para prever
        while int(count) < int(days):
            count += 1
            current_day += timedelta(days=1)
            data_covid.append(
                {
                    "id": index,
                    "date": str(current_day).split()[0],
                    "new_cases": -666,
                    "country_id": data_covid[0]["country_id"],
                }
            )
            index += 1

        return data_covid
