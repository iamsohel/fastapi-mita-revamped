from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.auth.service import RoleChecker, access_token_verify
from app.database.core import get_db

from .service import LanguageService
from .shemas import LanguageCreate, LanguageResponse, LanguageUpdate

language_router: APIRouter = APIRouter()

language_service = LanguageService()
role_checker = Depends(RoleChecker(["admin", "user"]))


@language_router.get("/", response_model=list[LanguageResponse])
async def get_all_languages(
    skip: int = 0,
    limit: int = 100,
    search: str = Query(None, alias="q"),  # Search by name
    sort_by: str = Query("id", enum=["id", "name"]),  # Sort field
    order: str = Query("asc", enum=["asc", "desc"]),  # Sort order
    db: Session = Depends(get_db),
):
    language = language_service.get_all_languages(
        db, skip, limit, search, sort_by, order
    )
    return language


@language_router.post("/", response_model=LanguageResponse, status_code=201)
async def create_language(language: LanguageCreate, db: Session = Depends(get_db)):
    return language_service.create_language(db, language)


@language_router.put("/{language_id}", response_model=LanguageResponse)
async def update_language(
    language_id: int, language: LanguageUpdate, db: Session = Depends(get_db)
):
    return language_service.update_language(db, language_id, language)


@language_router.delete(
    "/{language_id}", response_model=LanguageResponse, dependencies=[role_checker]
)
async def delete_language(
    language_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(access_token_verify),
):
    return language_service.delete_language(db, language_id)
