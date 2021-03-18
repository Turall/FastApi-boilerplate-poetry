from fastapi import APIRouter, HTTPException, status
from starlette.responses import JSONResponse
from app.utils.helpers import check_db_status


health_router = APIRouter()


@health_router.get("/health")
async def health():
    if await check_db_status():
        return JSONResponse(content={"result": True},status_code=status.HTTP_200_OK)
    
    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


@health_router.get("/readiness")
def readiness():
    return ""
