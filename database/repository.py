from database.engine import DBEngine
from abc import ABC, abstractmethod


class ConfigReaderBase(ABC):
    @abstractmethod
    def initial_config(self):
        NotImplementedError

    @abstractmethod
    def get_tokens(self):
        NotImplementedError

    @abstractmethod
    def set_lang(self):
        NotImplementedError

    @abstractmethod
    def get_base_params(self):
        NotImplementedError

    @abstractmethod
    def set_tokens(self):
        NotImplementedError


class ConfigReaderFromDB(ConfigReaderBase):
    def __init__(self):
        self.database = DBEngine()

    def initial_config(self):
        with self.database as cursor:
            cursor.executescript("""CREATE TABLE IF NOT EXISTS data
            (id integer unique default 1,
            api_base_url_cleaner text unique default 'https://cleaner.dadata.ru/',
            api_base_url_suggest text unique default 'https://suggestions.dadata.ru/',
            api_key text unique default NULL,
            secret_token text unique default NULL,
            lang text CHECK (lang in ('ru', 'en')) default 'ru');""")
            cursor.execute("INSERT OR IGNORE INTO data DEFAULT VALUES")

    def get_tokens(self):
        with self.database as cursor:
            cursor.execute("SELECT api_key, secret_token FROM data limit 1;")
            result = cursor.fetchone()
        return result

    def set_lang(self, lang: str):
        with self.database as cursor:
            cursor.execute("""UPDATE data
                            SET lang = ?
                            WHERE id = 1;""", ("ru" if lang == '1' else "en", ))

    def get_base_params(self):
        with self.database as cursor:
            cursor.execute("SELECT api_base_url_cleaner, api_base_url_suggest, lang FROM data limit 1;")
            result = cursor.fetchone()
        return result

    def set_tokens(self, api_key: str, secret_token):
        with self.database as cursor:
            cursor.execute("""UPDATE data
                            SET api_key = ?, secret_token = ?
                            WHERE id = 1;""", (api_key, secret_token, ))






