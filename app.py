from misc.repository import Repo
from misc.dadata_client import DadataClient


class DadataApp:
    repo = Repo()

    def __init__(self):
        self.repo.initial_table()

    def start(self):
        self._main_menu()

    def _main_menu(self):
        current_tokens = self.repo.get_tokens()
        if current_tokens[0] and current_tokens[1]:
            self._main_menu_with_token()
        else:
            self._main_menu_without_token()

    def _main_menu_with_token(self):
        print("Привет, дорогой")

    def _main_menu_without_token(self):
        self.repo.set_tokens(api_key=input("Введите api_key от сервиса dadata.ru: "),
                             secret_token=input("Введите token от сервиса dadata.ru: "))
        self.start()

    def _config_menu(self):
        pass

    def _api_query(self):
        pass




