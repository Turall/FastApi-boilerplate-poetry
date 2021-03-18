from starlette.config import Config
import os

project_name="test-service"


class BaseConfig:

    """
    Base configuration class. Subclasses should include configurations for
    testing, development and production environments
    """
    config = Config()

    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool, default=True)

    SECRET_KEY = config("SECRET_KEY",default=os.urandom(32))
    SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO",cast=bool,default=False)

    CORS_ORIGINS = config("CORS_HOSTS",default="*")

    DEBUG = config("DEBUG", cast=bool, default=True)
    TESTING = config("TESTING", cast=bool, default=False)

    API_VERSION = "v1"
    BASE_URL = f"/{project_name}/{API_VERSION}"
