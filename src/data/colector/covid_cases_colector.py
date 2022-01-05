"""Caso de uso para CovidCasesColector"""
from typing import List, Type, Dict
from src.data.interfaces import DataCovidConsumerInterface as DataCovidConsumer
from src.errors import HttpErrors
from src.domain.usecases import (
    CovidCasesColectorInterface,
    GetCountriesInterface as GetCountries,
)


class CovidCasesColector(CovidCasesColectorInterface):
    """DataCovidInformationColector usecase"""

    def __init__(
        self, api_consumer: Type[DataCovidConsumer], get_countries: Type[GetCountries]
    ) -> None:
        self.__api_consumer = api_consumer
        self.__get_countries = get_countries

    def covid_cases_country(self, country: str, days: int) -> List[Dict]:
        """
        Realiza o tratamento dos dados do covid por país recebidos do consumer.
        :param country: O país de referência que deverá ser tratado os dados.
               days: A quantidade de dias futuros que devem ser previstos.
        :return: Os dados do covid19 ja tratados e com uma previsão para os próximos dias.
        """

        country_exist = self.__get_countries.by_name(name=country)

        if not country_exist["success"]:
            http_error = HttpErrors.error_422()

            return [http_error]

        api_response = self.__api_consumer.get_data_covid_by_country(country).response

        country_data_response = self.__separete_data(api_response, days, country)

        return country_data_response

    def covid_cases_world(self, days: int) -> List[Dict]:
        """
        Realiza o tratamento dos dados do covid do mundo inteiro recebidos do consumer.
        :param days: A quantidade de dias futuros que devem ser previstos.
        :return: Os dados do covid19 ja tratados e com uma previsão para os próximos dias.
        """

        countries = self.__get_countries.all_countries()["data"][0]
        api_response = self.__api_consumer.get_all_data_covid().response

        countries_data = []

        for country in countries:

            country_data = api_response[country.name]
            each_country = self.__separete_data(country_data, days, country)

            countries_data.append(each_country)

            world_data_response = self.__world_data_sum(countries_data, days)

        return world_data_response

    @classmethod
    def __world_data_sum(cls, countries_data: List[List], days: int) -> List[Dict]:

        world_data_response = []

        for country in countries_data:
            for index, day in enumerate(country):

                date = day["date"]
                new_cases = day["new_cases"]

                if date == day["date"]:
                    new_cases += new_cases

                world_data_response.append(
                    {
                        "id": index,
                        "date": date,
                        "new_cases": new_cases,
                        "country": "WORLD",
                        "days": days,
                    }
                )

        return world_data_response

    @classmethod
    def __separete_data(
        cls, data_days: List[Dict], days: int, country: str = None
    ) -> List[Dict]:

        separate_data = []

        for index, day in enumerate(data_days):

            try:
                separate_data.append(
                    {
                        "id": index,
                        "date": day["date"],
                        "new_cases": day["new_cases"],
                        "country": country,
                        "days": days,
                    }
                )
            except KeyError:
                continue

        return separate_data


# import pandas as pd
# from numpy import mean

# @classmethod
# def __calculate_predict_covid_evolution(
#     cls, data_base: List[Dict], time: int
# ) -> List[Dict]:
#     """
#     Realiza a previsão de casos de covid nos proximos dias,
#     com base na média de casos dos últimos 7 dias.
#     :return: Uma lista com dados de previsão para cada dia,
#     baseado na quantidade de dias escolhido a partir da data atual.
#     """
#     # self.add_days_to_data_frame(time)
#     print(time)
#     data_frame = pd.DataFrame(data_base)

#     data_values = data_frame.values
#     window = 3

#     history = [data_values[i][2] for i in range(window)]
#     test = [data_values[i][2] for i in range(window, len(data_values))]
#     predicted = []
#     predicted_evolution = []
#     difference = 0

#     for index, value in enumerate(test):

#         length = len(history)
#         average_of_previous_days = mean(
#             [history[i] for i in range(length - window, length)]
#         )

#         # Adiciona 10% ou subtrai 15% ao suposto valor real de casos previstos,
#         # Dependendo da diferença entre o ultimo e penúltimo dos 7 dias anteriores.
#         if difference > 0:
#             hope = average_of_previous_days + (average_of_previous_days * 10 / 100)
#         else:
#             hope = average_of_previous_days - (average_of_previous_days * 15 / 100)

#         real_value = value
#         if value == -666:
#             real_value = hope

#         previous_days = [history[i] for i in range(length - window, length)]
#         difference = previous_days[-1] - previous_days[-2]

#         predicted.append(average_of_previous_days)
#         history.append(real_value)

#         # if datetime.strptime(data_values[index][1], "%Y-%m-%d") >= datetime.today():
#         predicted_evolution.append(
#             {
#                 "id": data_values[index][1],
#                 "date": data_values[index][0],
#                 "new_cases_real": real_value,
#                 "predicted_evolution": average_of_previous_days,
#             }
#         )
#     return predicted_evolution
