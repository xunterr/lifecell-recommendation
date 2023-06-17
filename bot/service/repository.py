from itertools import count
from asyncpg import UniqueViolationError
import psycopg2

class Repo:
    def __init__(self, conn):
        self.conn = conn

    # async def create_user_table(self):
    #     sql = """CREATE TABLE IF NOT EXISTS users
    #     (
    #         id uuid NOT NULL, PRIMARY KEY,
    #         username character varying NOT NULL,
    #         tariff_id integer PRYMARY KEY NOT NULL,
    #     )
    #     """
    #     await self.conn.execute(sql)



    # тут пишуть запити до бд, написав приклад     123

    