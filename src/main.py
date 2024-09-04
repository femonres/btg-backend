import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from interfaces.api.routers.user_routes import router as user_router
from interfaces.api.routers.fund_routes import router as fund_router
from logger.logger import setup_logger
from dotenv import load_dotenv

from utils.error_utils import log_info

# Carga de variables de entorno y configuración del logger
load_dotenv()
setup_logger()

# Configuración de la aplicación FastAPI
app = FastAPI(title="BTG Pactual Funds API")

# Configuración de CORS dependiendo del entorno
if os.getenv("ENVIRONMENT") == "production":
    allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
else:
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["Authorization", "Content-Type"]
)

@app.get("/")
async def read_root():
    log_info(message="Ingresando a la ruta raiz")
    return {"message": "BTG PActual Investmen"}

# Routers de la applicacion
app.include_router(user_router, prefix="/api/v1", tags=["Users"])
app.include_router(fund_router, prefix="/api/v1", tags=["Funds"])

# Adaptador para AWS Lambda
handler = Mangum(app)
