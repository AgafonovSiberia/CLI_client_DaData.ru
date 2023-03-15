
from misc.repository import Repo
from httpx import Client

class DadataClient:
    def __init__(self):
        self.repo = Repo()
        self._init_client_params()

        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": self.api_key,
            "X-secret": self.token
        }

        self._client = Client(base_url=self.base_url, headers=headers)

    def _init_client_params(self):
        self.api_key, self.token = self.repo.get_tokens()
        self.base_url, _ = self.repo.get_base_url()

    async def get_address(self, address: str):
        response = await self._client.post(url=f"{self.base_url}'/suggestions/api/4_1/rs/suggest/address'",
                                    data={"query": address})
        return response.json()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._client.close()

