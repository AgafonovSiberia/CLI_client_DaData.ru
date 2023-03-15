from misc.engine import DBEngine


class Repo:
    def __init__(self):
        self.database = DBEngine()

    def initial_table(self):
        with self.database as cursor:
            cursor.executescript("""CREATE TABLE IF NOT EXISTS data
            (id integer unique default 1,
            api_base_url text unique default 'https://cleaner.dadata.ru/',
            api_key text unique default NULL,
            secret_token text unique default NULL,
            lang text CHECK (lang in ('ru', 'en')) default 'ru');""")
            cursor.execute("INSERT OR IGNORE INTO data DEFAULT VALUES")

    def get_tokens(self):
        with self.database as cursor:
            cursor.execute("SELECT api_key, secret_token FROM data limit 1;")
            result = cursor.fetchone()
        return result

    def set_tokens(self, api_key: str, secret_token):
        with self.database as cursor:
            cursor.execute("""UPDATE data
                            SET api_key = ?, secret_token = ?
                            WHERE id = 1;""", (api_key, secret_token, ))






