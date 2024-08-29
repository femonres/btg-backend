import logging
import os
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() in ['true', '1', 'yes']

async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # Registra el error
        logger.error(f"Error occurred: {str(e)}")
        if DEBUG_MODE:
            # Captura detalles del error cuando estamos en modo de depuración
            error_details = {
                "message": str(e),
                "details": traceback.format_exc()
            }
        else:
            # Respuesta simplificada para producción
            error_details = {
                "message": "Internal Server Error"
            }
        return JSONResponse(
            status_code=500,
            content=error_details
        )

async def dispatch(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code == 404:
            return JSONResponse(
                status_code=404,
                content={"message": "The route you are looking for does not exist."},
            )
        return response
    except HTTPException as exc:
        if exc.status_code == 404:
            return JSONResponse(
                status_code=404,
                content={"message": "The route you are looking for does not exist."},
            )
        raise exc