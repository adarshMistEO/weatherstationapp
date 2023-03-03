from .database import collection_user as collection
from models.user import User
from fastapi.encoders import jsonable_encoder

async def fetch_user(id):
    document = await collection.find_one({"id": id})
    return document

async def fetch_all_user():
    users = []
    cursor = collection.find({})
    async for document in cursor:
        users.append(User(**document))
    return users

async def create_user(user):
    result = await collection.insert_one(jsonable_encoder(user))
    return result

async def update_user(id, user):
    await collection.update_one({"id": id}, {"$set": jsonable_encoder(user)})
    document = await collection.find_one({"id": id})
    return document

async def delete_user(id):
    await collection.delete_one({"id": id})
    return True