from .database import collection_location as collection
from models.location import Location
from fastapi.encoders import jsonable_encoder

async def fetch_location(id):
    document = await collection.find_one({"id": id})
    return document

async def fetch_all_location():
    locations = []
    cursor = collection.find({})
    async for document in cursor:
        locations.append(Location(**document))
    return locations

async def create_location(location):
    result = await collection.insert_one(jsonable_encoder(location))
    return result

async def update_location(id, location):
    await collection.update_one({"id": id}, {"$set": jsonable_encoder(location)})
    document = await collection.find_one({"id": id})
    return document

async def delete_location(id):
    await collection.delete_one({"id": id})
    return True