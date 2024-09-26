import psycopg # type: ignore
from contextlib import contextmanager

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self, user, password, host, database):
        if self.connection is None:
            self.connection = psycopg.connect(user=user, password=password, host=host, dbname=database)

    @contextmanager
    def get_connection(self):
        if self.connection is None:
            raise Exception("Database not connected")
        yield self.connection


db = Database()
db.connect('postgres', 'root', 'localhost', 'VentasControl')
