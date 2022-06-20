from motor.motor_asyncio import AsyncIOMotorClient
from main import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

BASE = declarative_base()


def start() -> scoped_session:
    engine = create_engine(DB_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URL is not configured. Features depending on the database might have issues."
    )
    print(str(e))


if not MONGO_DB:
    mongodb = AsyncIOMotorClient(MONGO_DB)
    db = mongodb["SPAMBOT"]
else:
    db = SqliteDatabase(DB_URL)
