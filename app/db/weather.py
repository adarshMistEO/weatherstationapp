from .database import collection_weather as collection
from models.weather import Weather
from fastapi.encoders import jsonable_encoder

async def fetch_weather(id):
    document  =await collection.find_one({"id": id})
    return document

async def fetch_all_weather():
    weather = []
    cursor = collection.find({})
    async for document in cursor:
        weather.append(Weather(**document))
    return weather

async def create_weather(weather):
    result = await collection.insert_one(jsonable_encoder(weather))
    return result

async def update_weather(id, weather):
    await collection.update_one({"id": id}, {"$set": jsonable_encoder(weather)})
    document = await collection.find_one({"id": id})
    return document

async def delete_weather(id):
    await collection.delete_one({"id": id})
    return True