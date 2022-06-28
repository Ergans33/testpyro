from pymongo import MongoClient
from pyrogram import Client
from pelerbot import MONGO_DB
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_


TEMP_MONGODB = "mongodb+srv://sanssss:sanssss@cluster0.xeqfq7q.mongodb.net/?retryWrites=true&w=majority"

if MONGO_DB is None:
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(MONGO_DB)
    _mongo_sync_ = MongoClient(MONGO_DB)
    mongodb = _mongo_async_.Sanssss
    pymongodb = _mongo_sync_.Sanssss
