from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.auth.views import auth_router
from app.language.views import language_router


class ErrorMessage(BaseModel):
    msg: str


class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)


@api_router.get("/healthcheck", include_in_schema=True)
def healthcheck():
    return {"status": "ok"}


api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(language_router, prefix="/languages", tags=["languages"])
# api_router.include_router(
#     post_router, tags=["posts"])
