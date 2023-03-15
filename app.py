from misc.repository import Repo
from misc.dadata_client import DadataClient

from misc.templates import main_menu
from misc.dadata_client import DadataClient


class DadataApp:
    def __init__(self):
        self.repo = Repo()
        self.client = DadataClient
        self.repo.initial_table()

    def start(self):
        self._main_menu()

    def _main_menu(self):
        id_key, token = self.repo.get_tokens()
        if id_key and token:
            return self._main_menu_with_token()
        return self._main_menu_without_token()


    def _main_menu_with_token(self):
        print(main_menu)
        command = int(input("Введите команду: "))
        if command == 1:
            self._api_query()


    def _main_menu_without_token(self):
        self.repo.set_tokens(api_key=input("Введите api_key от сервиса dadata.ru: "),
                             secret_token=input("Введите token от сервиса dadata.ru: "))
        self.start()

    def _config_menu(self):
        pass

    def _api_query(self):
        address = input("Введите искомый адрес: ")
        with self.client() as client:
            response = client.get_address(address)
            print(response)







