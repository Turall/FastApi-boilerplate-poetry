from starlette.config import Config
from sqlalchemy.engine.url import make_url
from starlette.datastructures import Secret,URL
from settings.settings import BaseConfig


class ProdSettings(BaseConfig):

    """ Configuration class for site production environment """

    config = Config()
    DEBUG = False
    DB_USER = config("DB_USER", cast=str)
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret)
    DB_HOST = config("DB_HOST", cast=str)
    DB_PORT = config("DB_PORT", cast=str)
    DB_NAME = config("DB_NAME", cast=str)
    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool)
    SSL_CERT_FILE = config("SSL_CERT_FILE")
    SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO",cast=bool,default=False)

    
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
