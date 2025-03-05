from pydantic import BaseModel, Field


class LanguageBase(BaseModel):
    name: str = Field(description="Name of the language")


class LanguageResponse(LanguageBase):
    id: int = Field(gt=0, description="id of the language")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "english",
                "lang_code": "en",
                "description": "this the language description",
            }
        }
    }


class LanguageCreate(LanguageBase):
    lang_code: str
    description: str


class LanguageUpdate(LanguageBase):
    lang_code: str
    description: str
