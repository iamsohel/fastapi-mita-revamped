from fastapi import HTTPException
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.language.shemas import LanguageCreate, LanguageUpdate
from app.models import Language


class LanguageService:
    def get_all_languages(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        search: str = None,
        sort_by: str = "id",
        order: str = "asc",
    ):
        query = db.query(Language)

        # Apply search filter
        if search:
            query = query.filter(
                Language.name.ilike(f"%{search}%")
            )  # Case-insensitive search

        # Apply sorting
        # Default to 'id' if invalid
        order_by_column = getattr(Language, sort_by, Language.id)
        query = query.order_by(
            asc(order_by_column) if order == "asc" else desc(order_by_column)
        )

        # Apply pagination
        languages = query.offset(skip).limit(limit).all()

        return languages

    def create_language(self, db: Session, language: LanguageCreate):
        db_language = Language(**language.model_dump())
        db.add(db_language)
        db.commit()
        db.refresh(db_language)
        return db_language

    def update_language(self, db: Session, language_id: int, language: LanguageUpdate):
        db_language = db.query(Language).filter(Language.id == language_id).first()

        if not db_language:
            raise HTTPException(status_code=404, detail="Language not found")

        language_data = language.model_dump(exclude_unset=True)

        for key, value in language_data.items():
            setattr(db_language, key, value)

        db.commit()
        db.refresh(db_language)
        return db_language

    def delete_language(self, db: Session, language_id: int):
        db_language = db.query(Language).filter(Language.id == language_id).first()

        if not db_language:
            raise HTTPException(status_code=404, detail="Language not found")
        db.delete(db_language)
        db.commit()
        return db_language
