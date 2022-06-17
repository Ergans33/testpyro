

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB

mongodb = AsyncIOMotorClient(MONGO_DB)
dbb = mongodb["SPAMBOT"]
