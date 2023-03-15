
from misc.repository import Repo
from httpx import Client
from abc import abstractmethod


class DadataClientBase:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @abstractmethod
    def close(self):
        NotImplementedError


class DadataClient(DadataClientBase):
    def __init__(self):
        self.repo = Repo()
        self._init_client_params()

        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {self.api_key}",
            "X-secret": self.token
        }

        self._client = Client(headers=headers)

    def _init_client_params(self):
        self.api_key, self.token = self.repo.get_tokens()
        self.base_url_cleaner, self.base_url_suggest, self.lang = self.repo.get_base_params()

    def get_address(self, address: str):
        response = self._client.post(url=f"{self.base_url_suggest}suggestions/api/4_1/rs/suggest/address",
                                     json={"query": address, "count": 20, "language": self.lang})
        return response.json()['suggestions']

    def get_location(self, address: str):
        response = self._client.post(url=f"{self.base_url_cleaner}api/v1/clean/address",
                                     json=[address])
        return response.json()[0]

    def close(self):
        self._client.close()

