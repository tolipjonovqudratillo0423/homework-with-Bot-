from psycopg2 import connect
from environs import Env


env = Env()
env.read_env()


def get_connect(query=None):
    return connect(
        user = env.str("DB_USER"),
        password = env.str("DB_PASSWORD"),
        database = env.str("DB"),
        port = env.str("DB_PORT"),
        host = env.str("DB_HOST")
    )
    



