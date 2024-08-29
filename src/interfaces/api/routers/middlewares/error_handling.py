from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": str(e)},
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