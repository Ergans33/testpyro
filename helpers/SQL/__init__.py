from motor.motor_asyncio import AsyncIOMotorClient
from config import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

BASE = declarative_base()


def start() -> scoped_session:
    engine = create_engine(DB_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


SESSION = start()
mongodb = AsyncIOMotorClient(MONGO_DB)
dbb = mongodb["SPAMBOT"]
