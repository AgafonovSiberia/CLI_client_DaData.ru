from config_reader import ConfigReaderFromDB
from templates import templates
from api.client import Client


class DadataApp:
    """
    CLI-App для работы с сервисом DaData.ru
    """

    def __init__(self):
        self.config = ConfigReaderFromDB()
        self.client_class = Client
        self.config.initial_config()

    def start(self):
        self._main_menu()

    def _main_menu(self):
        id_key, token = self.config.get_tokens()
        if id_key and token:
            return self._main_menu_with_token()
        return self._main_menu_without_token()

    def _main_menu_with_token(self):
        """Обработчик пользователя, токены которого определены в БД"""
        print(templates.main_menu)
        command = self._get_command(("1", "2", "0"))
        if command == "1":
            self._api_query_engine()
        elif command == "2":
            self._config_menu()
        elif command == "0":
            print(templates.bye_message)
            exit(0)

    def _main_menu_without_token(self):
        """Обработчик пользователя, токены которого не известны"""
        api_key = input(templates.input_api_key)
        secret_token = input(templates.input_token)

        with self.client_class() as client:
            is_valid = client.validate_tokens(api_key, secret_token)
            if is_valid:
                self.config.set_tokens(api_key, secret_token)
                return self.start()

        self._tokens_is_not_valid()

    def _tokens_is_not_valid(self):
        """Проверка на валидность токенов введённых пользователем"""
        print(templates.tokens_is_not_valid)
        command = self._get_command(("1", "0"))
        if command == "1":
            self._main_menu_without_token()
        elif command == "0":
            print(templates.bye_message)
            exit(0)

    def _config_menu(self):
        """Меню настроек"""
        print(templates.config_menu)
        command = self._get_command(("1", "2", "0"))
        if command == "1":
            self._main_menu_without_token()
        elif command == "2":
            self._change_lang_menu()
        elif command == "0":
            self._main_menu_with_token()

    def _change_lang_menu(self):
        """Меню смены языка"""
        print(templates.change_lang)
        command = self._get_command(("1", "2", "0"))
        if command in ("1", "2"):
            self.config.set_lang(command)
            print(f"{templates.change_lang}{'ru' if command== '1' else 'en'}")
            self._main_menu_with_token()
        elif command == "0":
            self._config_menu()

    def _change_lang_engine(self, new_lang: str = "en"):
        self.config.set_lang(lang=new_lang)

    def _api_query_engine(self):
        address_str = self._get_address_engine()
        if address_str:
            self._get_location_engine(address=address_str)
        self._main_menu()

    def _get_address_engine(self):
        """
        Запрашивает от пользователя адрес (в свободной форме).
        Получает от API набор подходящих адресов.
        Запрашивает у пользователя ID адреса, координаты которого
        нужно будет определить"""
        address = input(templates.input_address)
        if address == "0":
            return self._main_menu_with_token()
        print(templates.help_message_change_address)

        with self.client_class() as client:
            response = client.get_address(address)

        for idx, addr in enumerate(response, start=1):
            print(f"{idx} : {addr['unrestricted_value']}")

        address_idx = int(input(templates.input_address_idx))
        if address_idx == 0:
            return None
        return response[address_idx - 1]["value"]

    def _get_location_engine(self, address: str):
        """Получает от API координаты адреса"""
        with self.client_class() as client:
            response = client.get_location(address)
            print(templates.result)
            print(f"Адрес: {address}")
            print(
                f"Координаты:\nШирота: {response['geo_lat']},"
                f" Долгота: {response['geo_lon']}"
            )

    @staticmethod
    def _get_command(commands_list: tuple[str, ...]):
        command = None
        while command not in commands_list:
            command = input(templates.input_command)
            if command not in commands_list:
                print(templates.command_not_found)
        return command
