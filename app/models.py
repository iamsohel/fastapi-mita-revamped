# coding: utf-8
from sqlalchemy import (
    CHAR,
    JSON,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Table,
    Text,
    Time,
    UniqueConstraint,
    text,
)
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from app.database.core import Base

metadata = Base.metadata


class Advertisement(Base):
    __tablename__ = "advertisement"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('advertisement_id_seq'::regclass)"),
    )
    size = Column(BigInteger, nullable=False, comment="1:800*400,2:400*800")
    image = Column(Text)
    from_date = Column(DateTime)
    to_date = Column(DateTime)
    link = Column(Text)
    status = Column(Integer, server_default=text("1"))
    created_at = Column(DateTime)


class Attribute(Base):
    __tablename__ = "attributes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('attributes_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    name = Column(String(255))
    slug = Column(String(255), server_default=text("NULL::character varying"))
    description = Column(String(255))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class AttributesLanguage(Base):
    __tablename__ = "attributes_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('attributes_languages_id_seq'::regclass)"),
    )
    attribute_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class AttributesTranslation(Base):
    __tablename__ = "attributes_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('attributes_translations_id_seq'::regclass)"),
    )
    attribute_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Banner(Base):
    __tablename__ = "banners"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('banners_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    description = Column(Text)
    banner_type = Column(
        BigInteger,
        nullable=False,
        server_default=text("'0'::bigint"),
        comment="1: Text Only\n2 : Image / Offers\n3 : Ads",
    )
    image = Column(Text)
    quiz_id = Column(BigInteger)
    role_id = Column(
        Integer, nullable=False, server_default=text("0"), comment="0 : For All User"
    )
    platform = Column(
        Integer,
        nullable=False,
        server_default=text("0"),
        comment="0 : For All Platforms\n1 : Mobile\n2 : Website\n3 : Desktop App",
    )
    from_date = Column(DateTime, comment="banner will show from date")
    to_date = Column(DateTime, comment="banner will show to date")
    status = Column(Text, nullable=False, server_default=text("'1'::text"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    language_id = Column(Integer, nullable=False, server_default=text("1"))
    link = Column(Text)


class Category(Base):
    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('categories_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    parent_cat_id = Column(BigInteger, nullable=False)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), server_default=text("NULL::character varying"))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    image = Column(Text)
    description = Column(Text)
    parent_genre_id = Column(BigInteger, nullable=False, server_default=text("0"))


class CategoriesGenre(Base):
    __tablename__ = "categories_genres"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('categories_genres_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    category_id = Column(BigInteger, nullable=False)
    genre_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class CategoriesLanguage(Base):
    __tablename__ = "categories_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('categories_languages_id_seq'::regclass)"),
    )
    category_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class CategoriesTranslation(Base):
    __tablename__ = "categories_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('categories_translations_id_seq'::regclass)"),
    )
    category_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    slug = Column(String(255), server_default=text("NULL::character varying"))
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


t_cities = Table(
    "cities",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('cities_id_seq'::regclass)"),
    ),
    Column("country_id", Integer),
    Column("state_id", Integer),
    Column("name", Text),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)


t_complexities = Table(
    "complexities",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('complexities_id_seq'::regclass)"),
    ),
    Column("language_id", BigInteger),
    Column("name", Text, nullable=False),
    Column("slug", Text),
    Column("description", Text, nullable=False),
    Column("status", Text, nullable=False, server_default=text("'1'::text")),
    Column("is_deleted", Integer, nullable=False, server_default=text("0")),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("deleted_at", DateTime),
)


class ComplexitiesLanguage(Base):
    __tablename__ = "complexities_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('complexities_languages_id_seq'::regclass)"),
    )
    complexity_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class ComplexitiesTranslation(Base):
    __tablename__ = "complexities_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('complexities_translations_id_seq'::regclass)"),
    )
    complexity_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Country(Base):
    __tablename__ = "countries"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('countries_id_seq'::regclass)"),
    )
    region_id = Column(Integer)
    name = Column(Text)
    iso = Column(Text)
    dial_code = Column(Text)
    flag = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class FcmToken(Base):
    __tablename__ = "fcm_tokens"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('fcm_tokens_id_seq'::regclass)"),
    )
    user_id = Column(BigInteger, nullable=False)
    fcm_id = Column(Text, nullable=False)
    device_id = Column(Text, nullable=False)
    device_type = Column(Integer, nullable=False)
    type = Column(Integer)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class FlashQuizzesDeck(Base):
    __tablename__ = "flash_quizzes_decks"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    slug = Column(String(255), server_default=text("NULL::character varying"))
    quiz_deck_type_id = Column(BigInteger, nullable=False)
    quiz_deck_mode_id = Column(BigInteger, nullable=False)
    amount = Column(Text, server_default=text("0"))
    question_type_id = Column(BigInteger, server_default=text("0"))
    complexity_id = Column(BigInteger, nullable=False)
    can_add_hints = Column(Integer)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    created_by = Column(Integer, nullable=False)
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_published = Column(
        Integer, server_default=text("0"), comment="0: draft\n1: published"
    )
    total_quiz_takens = Column(BigInteger, server_default=text("0"))
    reviews = Column(BigInteger, server_default=text("0"))
    rating = Column(Numeric)
    timeperiod = Column(Time)
    is_official_quiz = Column(Integer, server_default=text("0"))


t_flash_quizzes_decks_levels = Table(
    "flash_quizzes_decks_levels",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('flash_quizzes_decks_levels_id_seq'::regclass)"),
    ),
    Column("quiz_deck_id", BigInteger, nullable=False),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("level_id", Integer),
)


class FlashQuizzesDecksMode(Base):
    __tablename__ = "flash_quizzes_decks_modes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_modes_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    can_download = Column(Integer, nullable=False)
    can_invite = Column(Integer, nullable=False)
    is_paid = Column(Integer, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


t_flash_quizzes_decks_question_types = Table(
    "flash_quizzes_decks_question_types",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text(
            "nextval('flash_quizzes_decks_question_types_id_seq'::regclass)"
        ),
    ),
    Column("name", Text, nullable=False),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)


class FlashQuizzesDecksType(Base):
    __tablename__ = "flash_quizzes_decks_types"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_types_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    description = Column(Text)
    status = Column(Integer, nullable=False, server_default=text("1"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Folder(Base):
    __tablename__ = "folders"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('folders_id_seq'::regclass)"),
    )
    parent_folder_id = Column(ForeignKey("folders.id", ondelete="CASCADE"))
    user_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    slug = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    parent_folder = relationship("Folder", remote_side=[id])


class Genre(Base):
    __tablename__ = "genre"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('genre_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    name = Column(Text, nullable=False)
    slug = Column(Text)
    description = Column(Text, nullable=False)
    image = Column(Text, nullable=False)
    status = Column(Text, nullable=False, server_default=text("'1'::text"))
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('keywords_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    name = Column(String(255), nullable=False)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class KeywordsLanguage(Base):
    __tablename__ = "keywords_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('keywords_languages_id_seq'::regclass)"),
    )
    keyword_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class KeywordsTranslation(Base):
    __tablename__ = "keywords_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('keywords_translations_id_seq'::regclass)"),
    )
    keyword_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Language(Base):
    __tablename__ = "languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('languages_id_seq'::regclass)"),
    )
    name = Column(String(255), nullable=False)
    lang_code = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    flag = Column(String(255), server_default=text("NULL::character varying"))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


t_levels = Table(
    "levels",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('levels_id_seq'::regclass)"),
    ),
    Column("language_id", Integer),
    Column("name", String(255)),
    Column("description", String(1000)),
    Column("genre_id", Integer, nullable=False),
    Column("category_id", Integer, nullable=False),
    Column("sub_category_id", Integer),
    Column("topic_id", Integer),
    Column(
        "status",
        String(255),
        nullable=False,
        server_default=text("'1'::character varying"),
    ),
    Column("is_deleted", Integer, nullable=False, server_default=text("0")),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("deleted_at", DateTime),
    Column("image", Text),
)


t_levels_translations = Table(
    "levels_translations",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('levels_translations_id_seq'::regclass)"),
    ),
    Column("language_id", Integer),
    Column("level_id", BigInteger, nullable=False),
    Column("name", String(255)),
    Column("description", String(1000)),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)


class MediaType(Base):
    __tablename__ = "media_types"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('media_types_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('notifications_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    from_user_id = Column(BigInteger)
    to_user_id = Column(BigInteger)
    title = Column(Text)
    content = Column(Text)
    attribute = Column(Text)
    value = Column(Text)
    notification_type = Column(Integer)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    image = Column(Text)
    is_read = Column(Integer, server_default=text("0"))


class OurUser(Base):
    __tablename__ = "our_users"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('our_users_id_seq'::regclass)"),
    )
    image = Column(String(255), nullable=False)
    url = Column(String(255))
    created_at = Column(TIMESTAMP(precision=6), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(precision=6), server_default=text("now()"))
    status = Column(Boolean, nullable=False, server_default=text("true"))
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))


class QuestionsAnsMode(Base):
    __tablename__ = "questions_ans_modes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('questions_ans_modes_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class QuestionsOptMode(Base):
    __tablename__ = "questions_opt_modes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('questions_opt_modes_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class QuestionsQusMode(Base):
    __tablename__ = "questions_qus_modes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('questions_qus_modes_id_seq'::regclass)"),
    )
    name = Column(Text, nullable=False)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class Session(Base):
    __tablename__ = "session"

    sid = Column(String, primary_key=True)
    sess = Column(JSON, nullable=False)
    expire = Column(TIMESTAMP(precision=6), nullable=False)


class Setting(Base):
    __tablename__ = "settings"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('settings_id_seq'::regclass)"),
    )
    name = Column(Text)
    from_value = Column(Text)
    to_value = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    key = Column(Text, nullable=False)


class State(Base):
    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('states_id_seq'::regclass)"),
    )
    country_id = Column(Integer)
    name = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('subscription_plans_id_seq'::regclass)"),
    )
    plan_name = Column(Text)
    months = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, server_default=text("1"))
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Upload(Base):
    __tablename__ = "upload"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('upload_id_seq'::regclass)"),
    )
    email = Column(String(255), nullable=False)
    file_name = Column(Text, nullable=False)
    total_records = Column(Integer, nullable=False)
    uploaded_records = Column(Integer, nullable=False)
    status = Column(Text, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    note = Column(Text)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))
    flash_quizzes_decks_id = Column(Integer)


class UserType(Base):
    __tablename__ = "user_types"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('user_types_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    status = Column(Integer, nullable=False, server_default=text("1"))
    can_subscribe = Column(Integer, nullable=False, server_default=text("0"))


class UsersPlansHistory(Base):
    __tablename__ = "users_plans_histories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_plans_histories_id_seq'::regclass)"),
    )
    user_id = Column(BigInteger, nullable=False)
    plan_id = Column(BigInteger, nullable=False)
    amount = Column(Numeric, nullable=False)
    payment_type = Column(Text)
    trxn_id = Column(Text)
    remarks = Column(Text)
    online_deduction_amount = Column(Numeric)
    payment_gateway_response = Column(Text)
    status = Column(Integer, nullable=False)
    custom_field = Column(Text)
    created_at = Column(DateTime)
    amount_tax = Column(Numeric, nullable=False, server_default=text("0"))


class WhatOurUserSay(Base):
    __tablename__ = "what_our_user_say"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('what_our_user_say_id_seq'::regclass)"),
    )
    first_name = Column(String(45), nullable=False)
    last_name = Column(CHAR(45), nullable=False)
    company_name = Column(String(45), nullable=False)
    designation = Column(String(45), nullable=False)
    content = Column(Text, nullable=False)
    company_logo = Column(Text, nullable=False)
    user_image = Column(Text, nullable=False)
    status = Column(Boolean, nullable=False, server_default=text("true"))
    is_deleted = Column(Boolean, server_default=text("false"))
    created_at = Column(TIMESTAMP(True, 6))
    updated_at = Column(TIMESTAMP(True, 6))
    deleted_at = Column(TIMESTAMP(True, 6))
    language_id = Column(BigInteger)


class AdvertisementCategory(Base):
    __tablename__ = "advertisement_categories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('advertisement_categories_id_seq'::regclass)"),
    )
    advertisement_id = Column(
        ForeignKey("advertisement.id", ondelete="CASCADE"), nullable=False
    )
    category_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    advertisement = relationship("Advertisement")


class AdvertisementGenre(Base):
    __tablename__ = "advertisement_genres"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('advertisement_genres_id_seq'::regclass)"),
    )
    advertisement_id = Column(
        ForeignKey("advertisement.id", ondelete="CASCADE"), nullable=False
    )
    genre_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    advertisement = relationship("Advertisement")


class AdvertisementLanguage(Base):
    __tablename__ = "advertisement_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('advertisement_languages_id_seq'::regclass)"),
    )
    advertisement_id = Column(ForeignKey("advertisement.id"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    advertisement = relationship("Advertisement")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('answers_id_seq'::regclass)"),
    )
    name = Column(Text)
    question_id = Column(BigInteger, nullable=False)
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    topic_id = Column(BigInteger, server_default=text("0"))
    language_id = Column(BigInteger, nullable=False)
    media_type = Column(Integer, nullable=False)
    file_path = Column(Text)
    is_right_answer = Column(Integer, nullable=False)
    status = Column(Text, nullable=False, server_default=text("'1'::text"))
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    ans_mode_id = Column(BigInteger)

    quiz_deck = relationship("FlashQuizzesDeck")


class CountriesTranslation(Base):
    __tablename__ = "countries_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('countries_translations_id_seq'::regclass)"),
    )
    countries_id = Column(ForeignKey("countries.id"), nullable=False)
    language_id = Column(ForeignKey("languages.id"), nullable=False)
    name = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    order_by = Column(Integer, server_default=text("0"))

    countries = relationship("Country")
    language = relationship("Language")


t_creator_terms_and_conditions = Table(
    "creator_terms_and_conditions",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('creator_terms_and_conditions_id_seq'::regclass)"),
    ),
    Column("language_id", ForeignKey("languages.id"), unique=True),
    Column("description", Text, nullable=False),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)


class Currency(Base):
    __tablename__ = "currency"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('currency_id_seq'::regclass)"),
    )
    currency_code = Column(Text)
    currency_symbol = Column(Text)
    description = Column(Text)
    language_id = Column(
        ForeignKey("languages.id"), nullable=False, server_default=text("1")
    )
    credit_to_currency_ratio = Column(Numeric, nullable=False, server_default=text("1"))

    language = relationship("Language")


class FlashQuizzesDecksAttribute(Base):
    __tablename__ = "flash_quizzes_decks_attributes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('flash_quizzes_decks_attributes_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    attribute_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksCategory(Base):
    __tablename__ = "flash_quizzes_decks_categories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('flash_quizzes_decks_categories_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    category_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksGenre(Base):
    __tablename__ = "flash_quizzes_decks_genres"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_genres_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    genre_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksInviteUser(Base):
    __tablename__ = "flash_quizzes_decks_invite_users"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('flash_quizzes_decks_invite_users_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksKeyword(Base):
    __tablename__ = "flash_quizzes_decks_keywords"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_keywords_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    keyword_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksLanguage(Base):
    __tablename__ = "flash_quizzes_decks_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('flash_quizzes_decks_languages_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksSubCategory(Base):
    __tablename__ = "flash_quizzes_decks_sub_categories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('flash_quizzes_decks_sub_categories_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    sub_category_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FlashQuizzesDecksTranslation(Base):
    __tablename__ = "flash_quizzes_decks_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('flash_quizzes_decks_translations_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class FoldersQuiz(Base):
    __tablename__ = "folders_quizzes"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('folders_quizzes_id_seq'::regclass)"),
    )
    folder_id = Column(ForeignKey("folders.id", ondelete="CASCADE"), nullable=False)
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    folder = relationship("Folder")
    quiz_deck = relationship("FlashQuizzesDeck")


class GenreLanguage(Base):
    __tablename__ = "genre_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('genre_languages_id_seq'::regclass)"),
    )
    genre_id = Column(ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    genre = relationship("Genre")


class GenreTranslation(Base):
    __tablename__ = "genre_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('genre_translations_id_seq'::regclass)"),
    )
    genre_id = Column(ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    genre = relationship("Genre")


class LanguagesTranslation(Base):
    __tablename__ = "languages_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('languages_translations_id_seq'::regclass)"),
    )
    in_language_id = Column(ForeignKey("languages.id"), nullable=False)
    language_id = Column(ForeignKey("languages.id"), nullable=False)
    lang_code = Column(String(255), nullable=False)
    flag = Column(String(255), server_default=text("NULL::character varying"))
    name = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    in_language = relationship(
        "Language", primaryjoin="LanguagesTranslation.in_language_id == Language.id"
    )
    language = relationship(
        "Language", primaryjoin="LanguagesTranslation.language_id == Language.id"
    )


class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('leaderboard_id_seq'::regclass)"),
    )
    user_id = Column(BigInteger, nullable=False)
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    points = Column(BigInteger, server_default=text("0"))
    no_of_played = Column(BigInteger, server_default=text("1"))
    accuracy = Column(Text, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


t_privacy_policy = Table(
    "privacy_policy",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('privacy_policy_id_seq'::regclass)"),
    ),
    Column("language_id", ForeignKey("languages.id"), unique=True),
    Column("description", Text, nullable=False),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)


class Question(Base):
    __tablename__ = "questions"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('questions_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    name = Column(Text, nullable=False)
    slug = Column(Text, nullable=False)
    explanation = Column(Text)
    hint = Column(Text)
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    topic_id = Column(BigInteger)
    qus_mode_id = Column(BigInteger, nullable=False)
    ans_mode_id = Column(BigInteger)
    opt_mode_id = Column(BigInteger)
    file_path = Column(Text)
    status = Column(Text, nullable=False, server_default=text("'1'::text"))
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    no_of_answers = Column(Integer, server_default=text("0"))

    quiz_deck = relationship("FlashQuizzesDeck")


class QuizzesTaken(Base):
    __tablename__ = "quizzes_takens"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('quizzes_takens_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    topic_id = Column(BigInteger, server_default=text("0"))
    user_id = Column(BigInteger, nullable=False)
    points = Column(BigInteger, server_default=text("0"))
    language_id = Column(BigInteger, nullable=False)
    accuracy = Column(Text, server_default=text("0"))
    total_hints_taken = Column(BigInteger, server_default=text("0"))
    total_time_taken = Column(Text, server_default=text("0"))
    total_right_answers = Column(BigInteger, server_default=text("0"))
    total_wrong_answers = Column(BigInteger, server_default=text("0"))
    total_skipped_answers = Column(BigInteger, server_default=text("0"))
    status = Column(
        Integer,
        server_default=text("1"),
        comment="1: Start, 2: Pause / Save / Quit, 3: Resume, 4: Complete",
    )
    flag1 = Column(Text, server_default=text("0"))
    flag2 = Column(Text, server_default=text("0"))
    flag3 = Column(Text, server_default=text("0"))
    flag4 = Column(Text, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


class ReviewsRating(Base):
    __tablename__ = "reviews_ratings"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('reviews_ratings_id_seq'::regclass)"),
    )
    from_user_id = Column(BigInteger, nullable=False)
    to_user_id = Column(BigInteger, server_default=text("0"))
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"),
        server_default=text("0"),
    )
    review = Column(Text)
    rating = Column(BigInteger, nullable=False)
    rating_for = Column(
        BigInteger, nullable=False, comment="1 : For Quiz Deck, 2 : For User"
    )
    status = Column(
        BigInteger, server_default=text("0"), comment="0 : Not Approved, 1 : Approved"
    )
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")


t_terms_and_conditions = Table(
    "terms_and_conditions",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text("nextval('terms_and_conditions_id_seq'::regclass)"),
    ),
    Column("language_id", ForeignKey("languages.id"), unique=True),
    Column("description", Text, nullable=False),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)


class Topic(Base):
    __tablename__ = "topics"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('topics_id_seq'::regclass)"),
    )
    language_id = Column(BigInteger)
    quiz_deck_id = Column(ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"))
    name = Column(String(255))
    slug = Column(String(255), server_default=text("NULL::character varying"))
    description = Column(String(1000))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    category_id = Column(ForeignKey("categories.id"))
    sub_category_id = Column(ForeignKey("categories.id"))
    genre_id = Column(ForeignKey("genre.id"))
    image = Column(Text)

    category = relationship("Category", primaryjoin="Topic.category_id == Category.id")
    genre = relationship("Genre")
    quiz_deck = relationship("FlashQuizzesDeck")
    sub_category = relationship(
        "Category", primaryjoin="Topic.sub_category_id == Category.id"
    )


class AnswersTranslation(Base):
    __tablename__ = "answers_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('answers_translations_id_seq'::regclass)"),
    )
    answer_id = Column(ForeignKey("answers.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text)
    media_type = Column(Integer, nullable=False)
    file_path = Column(Text)
    status = Column(Text, nullable=False, server_default=text("'1'::text"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    ans_mode_id = Column(BigInteger)

    answer = relationship("Answer")


class FlashQuizzesDecksTopic(Base):
    __tablename__ = "flash_quizzes_decks_topics"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_topics_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    topic_id = Column(ForeignKey("topics.id"))

    quiz_deck = relationship("FlashQuizzesDeck")
    topic = relationship("Topic")


class Plan(Base):
    __tablename__ = "plans"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('plans_id_seq'::regclass)"),
    )
    plan_name = Column(Text)
    amount = Column(Numeric, nullable=False)
    currency_id = Column(ForeignKey("currency.id"), nullable=False)
    credits = Column(BigInteger, nullable=False)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    stripe_product_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    stripe_price_id = Column(
        String(255), server_default=text("NULL::character varying")
    )

    currency = relationship("Currency")


class QuestionsTranslation(Base):
    __tablename__ = "questions_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('questions_translations_id_seq'::regclass)"),
    )
    question_id = Column(ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    name = Column(Text, nullable=False)
    slug = Column(Text)
    explanation = Column(Text)
    hint = Column(Text)
    file_path = Column(Text)
    status = Column(Integer, nullable=False, server_default=text("1"))
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    editor = Column(Text)

    question = relationship("Question")


class QuizzesResultsByQuestion(Base):
    __tablename__ = "quizzes_results_by_questions"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('quizzes_results_by_questions_id_seq'::regclass)"),
    )
    quiz_taken_id = Column(
        ForeignKey("quizzes_takens.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(BigInteger, nullable=False)
    language_id = Column(BigInteger, nullable=False)
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    topic_id = Column(BigInteger, server_default=text("0"))
    question_id = Column(BigInteger, nullable=False)
    selected_options = Column(Text)
    right_options = Column(Text)
    answer_mode = Column(BigInteger, nullable=False)
    option_mode = Column(BigInteger, nullable=False)
    status = Column(
        BigInteger,
        server_default=text("0"),
        comment="0 : skipped\n1 : right\n2 : wrong",
    )
    points = Column(BigInteger, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")
    quiz_taken = relationship("QuizzesTaken")


class SubscriptionPlansLanguage(Base):
    __tablename__ = "subscription_plans_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('subscription_plans_languages_id_seq'::regclass)"),
    )
    subscription_plan_id = Column(ForeignKey("subscription_plans.id"), nullable=False)
    language_id = Column(ForeignKey("languages.id"), nullable=False)
    currency_id = Column(ForeignKey("currency.id"), nullable=False)
    user_type_id = Column(ForeignKey("user_types.id"), nullable=False)
    plan_name = Column(Text)
    description = Column(Text)
    price_per_month = Column(Numeric, nullable=False)
    discount_percentage = Column(Integer, nullable=False)
    amount = Column(Numeric, nullable=False)
    status = Column(Integer, nullable=False, server_default=text("1"))
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    stripe_product_id = Column(String(255))
    stripe_price_id = Column(String(255))

    currency = relationship("Currency")
    language = relationship("Language")
    subscription_plan = relationship("SubscriptionPlan")
    user_type = relationship("UserType")


class TopicsTranslation(Base):
    __tablename__ = "topics_translations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('topics_translations_id_seq'::regclass)"),
    )
    topic_id = Column(ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(BigInteger)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    topic = relationship("Topic")


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_id_seq'::regclass)"),
    )
    user_type_id = Column(BigInteger)
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text)
    dial_code = Column(Text)
    is_email_verified = Column(
        String(255), nullable=False, server_default=text("'0'::character varying")
    )
    is_profile_completed = Column(
        String(255), nullable=False, server_default=text("'0'::character varying")
    )
    about_us = Column(String(255), server_default=text("NULL::character varying"))
    profile_pic = Column(Text)
    sign_up_medium = Column(
        String(255),
        server_default=text("NULL::character varying"),
        comment="1: Admin Panel\n2: Website\n3: Mobile\n4: Desktop App\n5: Facebook\n6: Twitter\n7: Google\n8: Line\n9: Linkedin",
    )
    facebook_oauth_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    twitter_oauth_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    linkedin_oauth_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    google_oauth_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    is_parent = Column(String(255), server_default=text("NULL::character varying"))
    parent_id = Column(BigInteger)
    language_id = Column(BigInteger)
    is_premium = Column(String(255), server_default=text("NULL::character varying"))
    subscription_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    otp = Column(Text)
    otp_generated_time = Column(DateTime)
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    referral_code = Column(Text)
    remember_token = Column(Text)
    line_oauth_id = Column(Text)
    total_quizzes = Column(BigInteger, nullable=False, server_default=text("0"))
    referred_by = Column(BigInteger, server_default=text("0"))
    country_id = Column(BigInteger)
    wallet_amount = Column(Numeric, server_default=text("0"))
    phone_no = Column(Numeric)
    stripe_customer_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    creator_kyc_status = Column(BigInteger, server_default=text("0"))
    currency_id = Column(ForeignKey("currency.id"), server_default=text("4"))
    name = Column(String(255), server_default=text("NULL::character varying"))

    currency = relationship("Currency")


t_flash_quizzes_decks_downloaded = Table(
    "flash_quizzes_decks_downloaded",
    metadata,
    Column(
        "id",
        Integer,
        nullable=False,
        server_default=text(
            "nextval('flash_quizzes_decks_downloaded_id_seq'::regclass)"
        ),
    ),
    Column("quiz_deck_id", ForeignKey("flash_quizzes_decks.id"), nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    UniqueConstraint("quiz_deck_id", "user_id"),
)


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('groups_group_id_seq'::regclass)"),
    )
    name = Column(String(255), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    slug = Column(String(255), server_default=text("NULL::character varying"))
    description = Column(Text, nullable=False)
    created_by = Column(ForeignKey("users.id"), nullable=False)
    type_of_payment = Column(Integer, nullable=False, server_default=text("0"))
    is_active = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    organization = Column(Text)
    profile_pic = Column(Text)
    open_close = Column(Integer, nullable=False, server_default=text("0"))

    user = relationship("User")


class InviteNonRegisteredUsersPrivateQuiz(Base):
    __tablename__ = "invite_non_registered_users_private_quiz"

    invitation_id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('invite_non_registered_users_private_quiz_invitation_id_seq'::regclass)"
        ),
    )
    quiz_deck_id = Column(ForeignKey("flash_quizzes_decks.id"), nullable=False)
    invitation_send_by = Column(ForeignKey("users.id"), nullable=False)
    email_id = Column(String(255), nullable=False)
    is_registered = Column(Integer, nullable=False, server_default=text("0"))

    user = relationship("User")
    quiz_deck = relationship("FlashQuizzesDeck")


class MyFavouriteQuizDeck(Base):
    __tablename__ = "my_favourite_quiz_decks"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('my_favourite_quiz_decks_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")
    user = relationship("User")


class MyPurchasedQuizDeck(Base):
    __tablename__ = "my_purchased_quiz_decks"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('my_purchased_quiz_decks_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime)
    language_id = Column(ForeignKey("languages.id"))

    language = relationship("Language")
    quiz_deck = relationship("FlashQuizzesDeck")
    user = relationship("User")


class MyTakeItLaterQuizDeck(Base):
    __tablename__ = "my_take_it_later_quiz_decks"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('my_take_it_later_quiz_decks_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(
        ForeignKey("flash_quizzes_decks.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")
    user = relationship("User")


class RemoveQuizDeck(Base):
    __tablename__ = "remove_quiz_deck"
    __table_args__ = (UniqueConstraint("quiz_deck_id", "user_id", "language_id"),)

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('remove_quiz_deck_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(ForeignKey("flash_quizzes_decks.id"), nullable=False)
    language_id = Column(ForeignKey("languages.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime)

    language = relationship("Language")
    quiz_deck = relationship("FlashQuizzesDeck")
    user = relationship("User")


class RepeatQuizzesDeck(Base):
    __tablename__ = "repeat_quizzes_decks"
    __table_args__ = (UniqueConstraint("quiz_deck_id", "user_id", "language_id"),)

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('repeat_quizzes_decks_id_seq'::regclass)"),
    )
    quiz_deck_id = Column(ForeignKey("flash_quizzes_decks.id"), nullable=False)
    language_id = Column(ForeignKey("languages.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime)

    language = relationship("Language")
    quiz_deck = relationship("FlashQuizzesDeck")
    user = relationship("User")


class Transfer(Base):
    __tablename__ = "transfer"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('transfer_id_seq'::regclass)"),
    )
    creator_id = Column(ForeignKey("users.id"), nullable=False)
    status = Column(Integer, server_default=text("1"))
    amount = Column(Numeric, nullable=False)
    currency_id = Column(ForeignKey("currency.id"), nullable=False)
    payment_type = Column(Text)
    trxn_id = Column(Text)
    payment_gateway_response = Column(Text)
    stripe_transfer_id = Column(
        String(255), server_default=text("NULL::character varying")
    )
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    creator = relationship("User")
    currency = relationship("Currency")


class UsersAbuseAndViolation(Base):
    __tablename__ = "users_abuse_and_violations"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_abuse_and_violations_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id"), nullable=False)
    name = Column(String(255), server_default=text("NULL::character varying"))
    email_id = Column(String(255), nullable=False)
    type_of_violation = Column(Text)
    violating_content = Column(Text)
    creator_name = Column(String(255), server_default=text("NULL::character varying"))
    quiz_deck_id = Column(ForeignKey("flash_quizzes_decks.id"), nullable=False)
    violation_details = Column(Text)
    comments = Column(Text)
    action = Column(Text)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    quiz_deck = relationship("FlashQuizzesDeck")
    user = relationship("User")


class UsersBankDetail(Base):
    __tablename__ = "users_bank_details"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_bank_details_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id"), nullable=False)
    citizenship = Column(Text)
    dob = Column(Date)
    address_line_1 = Column(Text)
    zip_code = Column(Text)
    indentity_doc = Column(Text)
    additional_email_id = Column(String(255))
    alternate_phone_number = Column(Numeric)
    account_owner_name = Column(String(255))
    account_number = Column(String(255))
    bank_name = Column(String(255))
    iban = Column(String(255))
    bank_address = Column(Text)
    bank_country = Column(Text)
    bank_country_code = Column(Text)
    bank_zip_code = Column(Text)
    profile_name = Column(String(255))
    profile_desc = Column(Text)
    created_at = Column(DateTime)
    branch_no = Column(String(255))
    swift_code = Column(String(255))
    branch_name = Column(Text)
    first_name_kana = Column(
        String(255), server_default=text("NULL::character varying")
    )
    last_name_kana = Column(String(255), server_default=text("NULL::character varying"))
    address_line_2 = Column(String(255), server_default=text("NULL::character varying"))
    city = Column(String(255), server_default=text("NULL::character varying"))
    state = Column(String(255), server_default=text("NULL::character varying"))
    town = Column(String(255), server_default=text("NULL::character varying"))

    user = relationship("User")


class UsersCategory(Base):
    __tablename__ = "users_categories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_categories_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category = relationship("Category")
    user = relationship("User")


class UsersEnquiry(Base):
    __tablename__ = "users_enquiries"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_enquiries_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id"))
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    email_id = Column(String(255), nullable=False)
    topic = Column(Text)
    comments = Column(Text)
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    user = relationship("User")


class UsersGenre(Base):
    __tablename__ = "users_genres"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_genres_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    genre_id = Column(ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    genre = relationship("Genre")
    user = relationship("User")


class UsersLanguage(Base):
    __tablename__ = "users_languages"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_languages_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship("User")


class UsersPaymentsHistory(Base):
    __tablename__ = "users_payments_histories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_payments_histories_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    quiz_deck_id = Column(BigInteger)
    plan_id = Column(BigInteger)
    trxn_id = Column(Text)
    remarks = Column(Text)
    wallet_deduction_amount = Column(Numeric)
    online_deduction_amount = Column(Numeric)
    amount = Column(Numeric, nullable=False)
    currency = Column(Text)
    payment_gateway_response = Column(Text)
    status = Column(
        Integer, nullable=False, comment="0:Intiated ,1:Processing ,2:Failed ,3:Success"
    )
    custom_field = Column(Text)
    created_at = Column(DateTime)

    user = relationship("User")


class UsersSubCategory(Base):
    __tablename__ = "users_sub_categories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_sub_categories_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id"), nullable=False)
    sub_category_id = Column(ForeignKey("categories.id"), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    sub_category = relationship("Category")
    user = relationship("User")


class UsersSubscriptionHistoriesOld(Base):
    __tablename__ = "users_subscription_histories_old"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('users_subscriptions_histories_id_seq'::regclass)"
        ),
    )
    user_subscription_id = Column(BigInteger)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    device_type = Column(Text)
    package_name = Column(Text)
    product_id = Column(Text)
    purchase_date_time = Column(DateTime)
    purchase_token = Column(Text)
    auto_renewing = Column(Integer, server_default=text("0"))
    receipt_data = Column(Text)
    receipt_password = Column(Text)
    exclude_old_transactions = Column(Text)
    trx_id = Column(Text)
    trx_status = Column(Integer, server_default=text("0"))
    amount = Column(Numeric, server_default=text("0"))
    currency = Column(Text)
    expired_at = Column(DateTime)
    expiry_days = Column(Text, server_default=text("'0'::text"))
    created_at = Column(DateTime)

    user = relationship("User")


class UsersSubscriptionPlansHistory(Base):
    __tablename__ = "users_subscription_plans_histories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('users_subscription_plans_histories_id_seq'::regclass)"
        ),
    )
    user_id = Column(ForeignKey("users.id"), nullable=False)
    subscription_plans_languages_id = Column(
        ForeignKey("subscription_plans_languages.id"), nullable=False
    )
    trxn_id = Column(Text)
    trxn_status = Column(Integer, server_default=text("0"))
    payment_type = Column(Text)
    amount = Column(Numeric, nullable=False)
    online_deduction_amount = Column(Numeric)
    payment_gateway_response = Column(Text)
    purchase_date_time = Column(DateTime)
    start_at = Column(DateTime)
    expired_at = Column(DateTime)
    auto_renewing = Column(Integer, server_default=text("0"))
    created_at = Column(DateTime)
    stripe_subscription_id = Column(String(255))
    stripe_subscription_status = Column(
        Integer, nullable=False, server_default=text("1")
    )
    stripe_schedule_id = Column(String(255))
    amount_tax = Column(Numeric, nullable=False, server_default=text("'0'::numeric"))
    updated_at = Column(DateTime)

    subscription_plans_languages = relationship("SubscriptionPlansLanguage")
    user = relationship("User")


class CreatorsCreditHistory(Base):
    __tablename__ = "creators_credit_histories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('creators_credit_histories_id_seq'::regclass)"),
    )
    creator_id = Column(ForeignKey("users.id"), nullable=False)
    credits = Column(Numeric, server_default=text("0"))
    my_purchased_quiz_decks_id = Column(ForeignKey("my_purchased_quiz_decks.id"))
    updated_balance = Column(Numeric, server_default=text("0"))
    trxn_type = Column(Integer)
    transfer_id = Column(ForeignKey("transfer.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    creator = relationship("User")
    my_purchased_quiz_decks = relationship("MyPurchasedQuizDeck")
    transfer = relationship("Transfer")


class FlashQuizzesDecksGroup(Base):
    __tablename__ = "flash_quizzes_decks_groups"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('flash_quizzes_decks_groups_id_seq'::regclass)"),
    )
    group_id = Column(ForeignKey("groups.group_id"), nullable=False)
    quiz_deck_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    group = relationship("Group")


class GroupsNew(Base):
    __tablename__ = "groups_news"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('groups_news_id_seq'::regclass)"),
    )
    group_id = Column(ForeignKey("groups.group_id"), nullable=False)
    created_by = Column(ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )

    user = relationship("User")
    group = relationship("Group")


class InviteEmailNotification(Base):
    __tablename__ = "invite_email_notifications"

    invitation_id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('invite_email_notifications_invitation_id_seq'::regclass)"
        ),
    )
    invitation_type = Column(Integer, nullable=False)
    from_user_id = Column(ForeignKey("users.id"))
    to_user_id = Column(ForeignKey("users.id"))
    group_id = Column(ForeignKey("groups.group_id"))
    quiz_deck_id = Column(ForeignKey("flash_quizzes_decks.id"))
    created_at = Column(DateTime)
    is_read = Column(Integer, server_default=text("0"))
    invitation_to_become_in_group = Column(Integer)

    from_user = relationship(
        "User", primaryjoin="InviteEmailNotification.from_user_id == User.id"
    )
    group = relationship("Group")
    quiz_deck = relationship("FlashQuizzesDeck")
    to_user = relationship(
        "User", primaryjoin="InviteEmailNotification.to_user_id == User.id"
    )


class InviteNonRegisteredUser(Base):
    __tablename__ = "invite_non_registered_users"

    invitation_id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('invite_non_registered_users_invitation_id_seq'::regclass)"
        ),
    )
    group_id = Column(ForeignKey("groups.group_id"))
    invitation_send_by = Column(ForeignKey("users.id"), nullable=False)
    email_id = Column(String(255), nullable=False)
    is_registered = Column(Integer, nullable=False, server_default=text("0"))

    group = relationship("Group")
    user = relationship("User")


class OpenGroupRequest(Base):
    __tablename__ = "open_group_request"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('open_group_request_id_seq'::regclass)"),
    )
    group_id = Column(ForeignKey("groups.group_id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime)

    group = relationship("Group")
    user = relationship("User")


class RemoveQuizDeckQuestion(Base):
    __tablename__ = "remove_quiz_deck_questions"
    __table_args__ = (UniqueConstraint("remove_quiz_deck_id", "question_id"),)

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('remove_quiz_deck_questions_id_seq'::regclass)"),
    )
    remove_quiz_deck_id = Column(ForeignKey("remove_quiz_deck.id"), nullable=False)
    question_id = Column(ForeignKey("questions.id"), nullable=False)
    created_at = Column(DateTime)
    quiz_taken_id = Column(ForeignKey("quizzes_takens.id"), nullable=False)

    question = relationship("Question")
    quiz_taken = relationship("QuizzesTaken")
    remove_quiz_deck = relationship("RemoveQuizDeck")


class RepeatQuizzesDeckQuestion(Base):
    __tablename__ = "repeat_quizzes_deck_questions"
    __table_args__ = (UniqueConstraint("repeat_quiz_deck_id", "question_id"),)

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('repeat_quizzes_deck_questions_id_seq'::regclass)"
        ),
    )
    repeat_quiz_deck_id = Column(ForeignKey("repeat_quizzes_decks.id"), nullable=False)
    question_id = Column(ForeignKey("questions.id"), nullable=False)
    created_at = Column(DateTime)

    question = relationship("Question")
    repeat_quiz_deck = relationship("RepeatQuizzesDeck")


class RepeatQuizzesTaken(Base):
    __tablename__ = "repeat_quizzes_takens"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('repeat_quizzes_takens_id_seq'::regclass)"),
    )
    repeat_quiz_deck_id = Column(ForeignKey("repeat_quizzes_decks.id"), nullable=False)
    topic_id = Column(BigInteger, server_default=text("0"))
    user_id = Column(BigInteger, nullable=False)
    points = Column(BigInteger, server_default=text("0"))
    language_id = Column(BigInteger, nullable=False)
    accuracy = Column(Text, server_default=text("0"))
    total_hints_taken = Column(BigInteger, server_default=text("0"))
    total_time_taken = Column(Text, server_default=text("0"))
    total_right_answers = Column(BigInteger, server_default=text("0"))
    total_wrong_answers = Column(BigInteger, server_default=text("0"))
    total_skipped_answers = Column(BigInteger, server_default=text("0"))
    status = Column(Integer, server_default=text("1"))
    flag1 = Column(Text, server_default=text("0"))
    flag2 = Column(Text, server_default=text("0"))
    flag3 = Column(Text, server_default=text("0"))
    flag4 = Column(Text, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    repeat_quiz_deck = relationship("RepeatQuizzesDeck")


class TransferDetail(Base):
    __tablename__ = "transfer_details"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('transfer_details_id_seq'::regclass)"),
    )
    transfer_id = Column(ForeignKey("transfer.id"), nullable=False)
    my_purchased_quiz_decks_id = Column(ForeignKey("my_purchased_quiz_decks.id"))
    created_at = Column(DateTime)

    my_purchased_quiz_decks = relationship("MyPurchasedQuizDeck")
    transfer = relationship("Transfer")


class UsersCreditHistory(Base):
    __tablename__ = "users_credit_histories"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_credit_histories_id_seq1'::regclass)"),
    )
    user_id = Column(BigInteger, nullable=False)
    plans_histories_id = Column(ForeignKey("users_plans_histories.id"))
    credits = Column(Numeric, server_default=text("0"))
    trxn_type = Column(Integer)
    is_referred = Column(Integer, server_default=text("0"))
    referred_user_id = Column(Integer)
    updated_balance = Column(Text)
    created_at = Column(DateTime)
    quiz_deck_id = Column(BigInteger)
    my_purchased_quiz_decks_id = Column(ForeignKey("my_purchased_quiz_decks.id"))

    my_purchased_quiz_decks = relationship("MyPurchasedQuizDeck")
    plans_histories = relationship("UsersPlansHistory")


class UsersCreditHistoriesOld(Base):
    __tablename__ = "users_credit_histories_old"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('users_credit_histories_id_seq'::regclass)"),
    )
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    payment_history_id = Column(
        ForeignKey("users_payments_histories.id", ondelete="CASCADE")
    )
    credits = Column(Numeric, server_default=text("0"))
    trxn_type = Column(Integer, comment="1:Credit ,2:Debit ,3:Refunded")
    is_referred = Column(Integer, server_default=text("0"))
    referred_user_id = Column(Integer)
    updated_balance = Column(Text)
    created_at = Column(DateTime)
    quiz_deck_id = Column(BigInteger)

    payment_history = relationship("UsersPaymentsHistory")
    user = relationship("User")


class UsersGroup(Base):
    __tablename__ = "users_groups"

    group_id = Column(ForeignKey("groups.group_id"), primary_key=True, nullable=False)
    user_id = Column(ForeignKey("users.id"), primary_key=True, nullable=False)
    is_admin = Column(Integer, nullable=False, server_default=text("0"))
    is_priviledged_member = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_deleted = Column(Integer, nullable=False, server_default=text("0"))
    status = Column(
        String(255), nullable=False, server_default=text("'1'::character varying")
    )
    can_create_content = Column(Integer, server_default=text("0"))
    can_post_news = Column(Integer, server_default=text("0"))

    group = relationship("Group")
    user = relationship("User")


class UsersSubscriptionPlansHistoriesDetail(Base):
    __tablename__ = "users_subscription_plans_histories_details"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('users_subscription_plans_histories_details_id_seq'::regclass)"
        ),
    )
    users_subscription_plans_histories_id = Column(
        ForeignKey("users_subscription_plans_histories.id"), nullable=False
    )
    start_at = Column(DateTime)
    expired_at = Column(DateTime)
    payment_gateway_response = Column(Text)
    trxn_id = Column(Text)

    users_subscription_plans_histories = relationship("UsersSubscriptionPlansHistory")


class RepeatQuizzesResultsByQuestion(Base):
    __tablename__ = "repeat_quizzes_results_by_questions"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text(
            "nextval('repeat_quizzes_results_by_questions_id_seq'::regclass)"
        ),
    )
    repeat_quiz_taken_id = Column(
        ForeignKey("repeat_quizzes_takens.id"), nullable=False
    )
    repeat_quiz_deck_id = Column(ForeignKey("repeat_quizzes_decks.id"), nullable=False)
    user_id = Column(BigInteger, nullable=False)
    topic_id = Column(BigInteger, server_default=text("0"))
    question_id = Column(ForeignKey("questions.id"), nullable=False)
    language_id = Column(BigInteger, nullable=False)
    selected_options = Column(Text)
    right_options = Column(Text)
    answer_mode = Column(BigInteger, nullable=False)
    option_mode = Column(BigInteger, nullable=False)
    status = Column(BigInteger, server_default=text("0"))
    points = Column(BigInteger, server_default=text("0"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    question = relationship("Question")
    repeat_quiz_deck = relationship("RepeatQuizzesDeck")
    repeat_quiz_taken = relationship("RepeatQuizzesTaken")
