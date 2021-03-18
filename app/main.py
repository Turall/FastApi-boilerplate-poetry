import time, random, string, logging
from fastapi import FastAPI, Depends
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from core.factories import settings
from core.extensions import db
from app.utils.dependency import has_access
from app.controllers.protected_controller import router
from app.controllers.health_controller import health_router

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


app = FastAPI(
    docs_url=settings.BASE_URL + "/docs",
    openapi_url=settings.BASE_URL + "/openapi.json",
)

db.init_app(app)
log = logging.getLogger()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    log.info(
        f"RID={idem} START REQUEST PATH={request.url.path} METHOD={request.method} "
    )
    start_time = time.time()
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    log.info(
        f"RID={idem} COMPLETED={formatted_process_time}ms REQUEST={request.method.upper()} {request.url.path} STATUS_CODE={response.status_code}"
    )

    return response


def modify_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="microservice",
        version=settings.API_VERSION,
        description="Operations",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = modify_openapi


@app.on_event("startup")
async def startup():
    print("app started")


@app.on_event("shutdown")
async def shutdown():
    print("SHUTDOWN")


cors_origins = [i.strip() for i in settings.CORS_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix=settings.BASE_URL, tags=["Protected"] ,dependencies=[Depends(has_access)])
app.include_router(health_router, prefix=settings.BASE_URL, tags=["Health check"])
