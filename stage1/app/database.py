from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Session
from collections.abc import Generator

class Base(DeclarativeBase):
    pass
engine=create_engine(
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    echo=True,
)
SessionLocal = sessionmaker(bind=engine)

def get_db()->Generator[Session,None,None]:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
