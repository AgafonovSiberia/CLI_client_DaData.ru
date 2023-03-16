from config_reader import ConfigReaderFromDB
from httpx import Client as HttpClient
from abc import abstractmethod


TEST_ADDRESS = "Новосибирск проспект Карла Маркса, 30/1"


class ClientBase:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @abstractmethod
    def close(self):
        NotImplementedError


class Client(ClientBase):
    """
    Клиент для работы с API сервиса DaData.ru
    """

    def __init__(self):
        self.config = ConfigReaderFromDB()
        headers = {"Content-type": "application/json", "Accept": "application/json"}

        self._client = HttpClient(headers=headers)
        self._init_client_params()

    def _init_client_params(self) -> None:
        """
        Инициализация параметров http-клиента
        """
        self.api_key, self.token = self.config.get_tokens()
        if self.api_key:
            self._client.headers["Authorization"] = f"Token {self.api_key}"
            self._client.headers["X-secret"] = self.token

        (
            self.base_url_cleaner,
            self.base_url_suggest,
            self.lang,
        ) = self.config.get_base_params()

    def get_address(self, address: str) -> dict:
        """
        Получает от API сервиса DaData.ru адреса,
        которые максимально приближены к пользовательскому запросу.
        https://dadata.ru/api/suggest/address/

        :param address: адрес, введённый пользователем в свободной форме
        :return: словарь с данными по 20 адресам
        """
        response = self._client.post(
            url=f"{self.base_url_suggest}/address",
            json={"query": address, "count": 20, "language": self.lang},
        )
        return response.json()["suggestions"]

    def get_location(self, address: str) -> dict:
        """
        Получает от API сервиса DaData.ru координаты по адресу.
        Адрес выбирается пользователем из набора, который вернёт self.get_address
        https://dadata.ru/api/geocode/

        :param address: строка с полным адресом
        :return: словарь с данными по адресу, включая координаты
        """
        response = self._client.post(
            url=f"{self.base_url_cleaner}/address", json=[address]
        )
        return response.json()[0]

    def validate_tokens(self, api_key: str, token: str) -> bool:
        """
        Позволяет проверить введённые пользователем данные на валидность.
        403 - код ответа сервиса ("В запросе указан несуществующий API-ключ
        или не подтверждена почта или исчерпан дневной лимит по количеству запросов")

        :param api_key: API-ключ от сервиса DaData.ru
        :param token: Token от сервиса DaData.ru
        :return: False, если данные не валидны, True в обратном случае
        """
        response = self._client.post(
            url=f"{self.base_url_cleaner}/address",
            json=[TEST_ADDRESS],
            headers={"Authorization": f"Token {api_key}", "X-secret": token},
        )
        if response.status_code == 403:
            return False
        return True

    def close(self) -> None:
        self._client.close()
