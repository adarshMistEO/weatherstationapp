#MongoDB driver
import motor.motor_asyncio
from models.weather import Weather

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://adarsh0215:<6Dk0mwn4BD5ixng3>@cluster0.8simsnn.mongodb.net/?retryWrites=true&w=majority')

database = client.WeatherReport
collection_weather = database.weather
collection_location = database.location
collection_user = database.user

