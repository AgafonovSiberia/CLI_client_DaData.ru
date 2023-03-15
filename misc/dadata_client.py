from aiohttp import ClientSession
from misc.repository import Repo


class DadataClient:
    repo = Repo()

    def __init__(self, token: str, base_url: str):
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": token,
        }

        self._client = ClientSession(base_url=base_url, headers=headers)


