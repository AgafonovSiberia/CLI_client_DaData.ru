from database.repository import Repo
from templates import templates
from api.client import Client


class DadataApp:
    def __init__(self):
        self.repo = Repo()
        self.client_class = Client
        self.repo.initial_config()

    def start(self):
        self._main_menu()

    def _main_menu(self):
        id_key, token = self.repo.get_tokens()
        if id_key and token:
            return self._main_menu_with_token()
        return self._main_menu_without_token()

    def _main_menu_with_token(self):
        print(templates.main_menu)
        command = self._get_command(("1", "2", "3"))
        if command == "1":
            self._api_query_engine()
        elif command == "2":
            self._config_menu()
        elif command == "3":
            print("Всего доброго!")
            exit(0)

    def _main_menu_without_token(self):
        self.repo.set_tokens(api_key=input("Введите api_key от сервиса dadata.ru: "),
                             secret_token=input("Введите token от сервиса dadata.ru: "))
        self.start()

    def _config_menu(self):
        print(templates.config_menu)
        command = self._get_command(("1", "2", "3"))
        if command == "1":
            self._main_menu_withot_token()
        elif command == "2":
            self._change_lang_menu()
        elif command == "3":
            self._main_menu_with_token()


    def _change_lang_menu(self):
        print(templates.change_lang)
        command = self._get_command(("1", "2", "3"))
        if command in ("1", "2"):
            self.repo.set_lang(command)
        elif command == "3":
            self._config_menu()

    def _change_lang_engine(self, new_lang: str = "en"):
        self.repo.set_lang(lang=new_lang)

    def _api_query_engine(self):
        address_str = self._get_address_engine()
        self._get_location_engine(address=address_str)
        self._main_menu()

    def _get_address_engine(self):
        address = input("Введите искомый адрес в свободной форме: ")
        print("Пожалуйста, выберите один из найденных адресов")
        with self.client_class() as client:
            response = client.get_address(address)
            for idx, addr in enumerate(response, start=1):
                print(f"{idx} : {addr['unrestricted_value']}")

        address_idx = int(input("Введите ID подходящего адреса: "))
        return response[address_idx - 1]['value']

    def _get_location_engine(self, address: str):
        with self.client_class() as client:
            response = client.get_location(address)
            print(response["geo_lat"], response["geo_lon"])

    @staticmethod
    def _get_command(commands_list: tuple[str], command: int = None):
        while command not in commands_list:
            command = input("Введите команду: ")
            if command not in commands_list:
                print("Command not found")
        return command

















