from fastapi import FastAPI

from interfaces.api.routers.user_routes import router as user_router
from interfaces.api.routers.fund_routes import router as fund_router
from logger.logger import setup_logger

setup_logger()

app = FastAPI(title="BTG Pactual Funds API")
app.include_router(user_router, prefix="/api/v1", tags=["Users"])
app.include_router(fund_router, prefix="/api/v1", tags=["Funds"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")