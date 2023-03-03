from pydantic import BaseModel

class Weather(BaseModel):
    id: int
    temperature: int
    humidity: int
    windspeed:int
    precipitation: int
    pressure: int

    class Config:
        orm_mode = True