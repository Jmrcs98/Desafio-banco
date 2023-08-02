import psycopg2
from psycopg2 import Error


class DatabaseConnection:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(self.connection.get_dsn_parameters(), '\n')

            self.cursor.execute('SELECT version();')
            record = self.cursor.fetchone()
            print('You are connected to - ', record, '\n')

        except (Exception, Error) as e:
            print('Error while connecting to Postgres', e)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
