from typing import Dict, Type
from src.domain.usecases import DataCovidListColectorInterface
from src.infra import DataCovidConsumer


class DataCovidListColector(DataCovidListColectorInterface):
    """Casos de uso para DataCovidListColector"""

    def __init__(self, api_consumer: Type[DataCovidConsumer]) -> None:
        self.__api_consumer = api_consumer

    def list(self) -> Dict:
        response = self.__api_consumer.get_data_covid()
        print(response)
