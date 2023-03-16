import sqlite3


class SQLiteEngine:
    """
    Реализация контекстного менеджера для SQlite
    """
    def __init__(self, database_file: str = "data.db"):
        self.database_file = database_file

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_file)
        return self.connection.cursor()

    def __exit__(self, exception_type, exception_value, traceback):
        self.connection.commit()
        self.connection.close()

