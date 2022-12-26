import sqlite3
from sqlite3.dbapi2 import Connection

from models.user import User

DATABASE_NAME = 'thoughts.db'


class DatabaseHandler:
    def __init__(self):
        self.connection: Connection = None

    def initialize(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        print('Connected to database successfully')

        self.__create_users_table()
        self._create_thoughts_table()

    def get_user(self, user_id):
        query = f"select * from USERS where ID = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (user_id,))
        users = cursor.fetchall()

        if len(users) == 0:
            user = None
        else:
            user = User(users[0][0])

        cursor.close()
        return user

    def create_user(self, user_id):
        query = f"""insert into USERS
                (ID)
                VALUES
                ({user_id})"""

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

        return User(user_id)

    def __create_users_table(self):
        self.connection.execute('''CREATE TABLE IF NOT EXISTS USERS
        (ID INT PRIMARY KEY     NOT NULL);''')

        print('Users table created')

    def _create_thoughts_table(self):
        self.connection.execute('''CREATE TABLE IF NOT EXISTS THOUGHTS
        (ID INT PRIMARY KEY     NOT NULL,
        TEXT           TEXT    NOT NULL,
        AUTHOR         TEXT    NOT NULL,
        USER_ID        INT     NOT NULL);''')

        print('Thoughts table created')
