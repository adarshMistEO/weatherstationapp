from pydantic import BaseModel

class Location(BaseModel):
    id: int
    latitude: float
    longitude: float
    city: str
    state:  str
    country: str
    
    class Config:
        orm_mode = True