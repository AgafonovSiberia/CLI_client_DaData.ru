
from database.repository import ConfigReaderFromDB
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
    def __init__(self):
        self.config = ConfigReaderFromDB()
        self._init_client_params()

        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {self.api_key}",
            "X-secret": self.token
        }

        self._client = HttpClient(headers=headers)

    def _init_client_params(self):
        self.api_key, self.token = self.config.get_tokens()
        self.base_url_cleaner, self.base_url_suggest, self.lang = self.config.get_base_params()

    def get_address(self, address: str):
        response = self._client.post(url=f"{self.base_url_suggest}suggestions/api/4_1/rs/suggest/address",
                                     json={"query": address, "count": 20, "language": self.lang})
        return response.json()['suggestions']

    def get_location(self, address: str):
        response = self._client.post(url=f"{self.base_url_cleaner}api/v1/clean/address",
                                     json=[address])
        return response.json()[0]

    def validate_tokens(self, api_key: str, token: str):
        response = self._client.post(url=f"{self.base_url_cleaner}api/v1/clean/address",
                                     json=[TEST_ADDRESS],
                                     headers={"Authorization": f"Token {api_key}",
                                              "X-secret": token})
        if response.status_code == 403:
            return False
        return True

    def close(self):
        self._client.close()
