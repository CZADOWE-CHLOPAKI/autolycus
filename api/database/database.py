import motor.motor_asyncio
from bson import ObjectId
from pymongo import MongoClient

from .database_helper import user_helper
from ..config.config import MONGO_CONNECTION_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONNECTION_URL)
# client = MongoClient('mongo', 27017)

database = client.maps

user_collection = database.get_collection('users')


async def retrieve_users():
    users = []
    async for User in user_collection.find():
        users.append(user_helper(User))
    return users


async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


async def retrieve_user(user_id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)


async def delete_user(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(user_id)})
        return True


async def update_user_data(user_id: str, data: dict):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
        return True
