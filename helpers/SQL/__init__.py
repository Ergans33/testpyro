from motor.motor_asyncio import AsyncIOMotorClient
from config import *

mongodb = AsyncIOMotorClient(MONGO_DB)
dbb = mongodb["SPAMBOT"]
