from gino.ext.starlette import Gino
from ssl import create_default_context
from fastapi.security import HTTPBearer
from core.factories import settings


if not settings.DEBUG:
    ssl_object = create_default_context(cafile=settings.SSL_CERT_FILE)

    db: Gino = Gino(
        dsn=settings.DATABASE_URL,
        echo=settings.SQLALCHEMY_ECHO,
        ssl=ssl_object,
        pool_min_size=3,
        pool_max_size=20,
        retry_limit=1,
        retry_interval=1,
    )
else:
    db: Gino = Gino(dsn=settings.DATABASE_URL)


security = HTTPBearer()