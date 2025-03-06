import json
import logging
import time
from datetime import datetime

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import StreamingResponse

from app.api import api_router
from app.logging import configure_logging
from app.rate_limiter import limiter

# ========== 🔹 CONFIGURE LOGGING ==========
configure_logging()
log = logging.getLogger(__name__)

# ========== 🔹 EXCEPTION HANDLERS ==========


async def not_found(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": [{"msg": exc.detail or "Not found"}]},
    )


async def global_exception_handler(request: Request, exc: Exception):
    """Handles unexpected/unhandled exceptions"""
    log.error(f"Unhandled Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": [{"msg": "Internal Server Error"}]},
    )


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> StreamingResponse:
        try:
            response = await call_next(request)
        except ValidationError as e:
            log.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={"detail": e.errors()},
            )
        except ValueError as e:
            log.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,  # Use 400 for bad requests
                content={"detail": [{"msg": str(e), "type": "ValueError"}]},
            )
        except Exception as e:
            log.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": [{"msg": "Internal Server Error"}]},
            )
        return response


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.utcnow()
        response = await call_next(request)
        process_time = (datetime.utcnow() - start_time).total_seconds()
        log.info(
            json.dumps(
                {
                    "method": request.method,
                    "url": str(request.url),
                    "status_code": response.status_code,
                    "process_time": f"{process_time:.4f}s",
                }
            )
        )
        return response


# ========== 🔹 APP INSTANCE ==========
exception_handlers = {404: not_found}
app = FastAPI(
    title="MyAPI",
    description="Welcome to MyAPI's API documentation! Here you will be able to discover all of the ways you can interact with the MyAPI API.",
    root_path="/api/v1",
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
    exception_handlers=exception_handlers,
)

# ========== 🔹 SECURITY ENHANCEMENTS ==========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Change to your frontend domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=["yourdomain.com"])
# app.add_middleware(HTTPSRedirectMiddleware)  # Redirect HTTP → HTTPS

# ========== 🔹 MIDDLEWARE ==========
app.add_middleware(ExceptionMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)


@app.middleware("http")
async def custom_logging(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    processing_time = time.time() - start_time

    message = f"{request.client.host}:{request.client.port} - {request.method} - {request.url.path} - {response.status_code} completed after {processing_time}s"

    print(message)
    return response


# ========== 🔹 RATE LIMITING ==========
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ========== 🔹 REGISTER API ROUTES ==========
app.include_router(api_router)

# ========== 🔹 GRACEFUL SHUTDOWN ==========


@app.on_event("startup")
async def startup_event():
    log.info("Application is starting...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Application is shutting down...")
    # If using a database engine, ensure cleanup
    # await engine.dispose()
