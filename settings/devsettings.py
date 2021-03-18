from starlette.config import Config
from starlette.datastructures import Secret
from sqlalchemy.engine.url import make_url, URL
from settings.settings import BaseConfig


class DevSettings(BaseConfig):

    """ Configuration class for site development environment """

    config = Config(".env")
    DEBUG = True
    DB_USER = config("DB_USER", cast=str, default="postgres")
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default="postgres")
    DB_HOST = config("DB_HOST", cast=str, default="db")
    DB_PORT = config("DB_PORT", cast=str, default="5432")
    DB_NAME = config("DB_NAME", cast=str, default="postgres")
    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool, default=False)
    DATABASE_URL = config(
    "DATABASE_URL",
    cast=make_url,
    default=URL(
        drivername="asyncpg",
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    ),
)