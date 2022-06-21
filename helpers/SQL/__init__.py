from motor.motor_asyncio import AsyncIOMotorClient
from main import *
from config import *
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

BASE = declarative_base()


def start() -> scoped_session:
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

SESSION = start()


if not MONGO_DB:
    mongodb = AsyncIOMotorClient(MONGO_DB)
    db = mongodb["SPAMBOT"]
else:
    db = SqliteDatabase(DB_URI)
