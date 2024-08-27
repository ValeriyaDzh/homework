from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def create_db():
    Base.metadata.create_all(engine)
