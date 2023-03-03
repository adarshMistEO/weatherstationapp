from fastapi import Depends, HTTPException, Security, status
from fastapi import APIRouter
from models.weather import Weather
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db.weather import (
    fetch_weather,
    fetch_all_weather,
    create_weather,
    update_weather,
    delete_weather,
)

router = APIRouter()
security = HTTPBearer()

@router.get("/weather")
async def get_weather(credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await fetch_all_weather()
    return response

@router.get("/weather{id}", response_model=Weather)
async def get_weather_report_by_id(id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await fetch_weather(id)
    if response:
      return response
    raise HTTPException(status_code=404,  detail="Weather report with id {id} not found")

@router.post('/weather', status_code=200)
async def add_weather_report(details: Weather, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await create_weather(details.dict())
    if response:
        return {
            'code': 200,
            'message': 'Weather report added successfully',
        } 
    raise HTTPException(status_code=400,  detail="Bad Request : Invalid argument (invalid request payload)")

@router.put('/weather{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_weather_report(id: int, details: Weather, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await update_weather(id, details.dict())
    if response:
        return {
            'code': 200,
            'message': 'Weather updated successfully',
        } 
    raise HTTPException(status_code=404, detail="Weather report not found")

@router.delete('/weather{id}')
async def delete_weather_report(id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await delete_weather(id)
    if response:
        return "Succesfully deleted"
    raise HTTPException(status_code=204, detail="Weather report not found")
