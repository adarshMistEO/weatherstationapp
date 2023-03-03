from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.location import Location
from db.location import (
    fetch_location,
    fetch_all_location,
    create_location,
    update_location,
    delete_location,
)

router = APIRouter()
security = HTTPBearer()

@router.get("/location")
async def all_location(credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await fetch_all_location()
    return response

@router.get("/location{id}", response_model=Location)
async def get_location_by_id(id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await fetch_location(id)

    if response:
      return response
    raise HTTPException(status_code=404, detail="Location with id {id} not found")

@router.post('/location', status_code=200)
async def add_location(details: Location, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await create_location(details.dict())
    if response:
        return {
            'code': 200,
            'message': 'Location added successfully',
        } 
    raise HTTPException(status_code=200, detail="Bad Request")

@router.put('/location{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_location_by_id(id: int, details: Location, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await update_location(id, details.dict())
    if response:
        return {
            'code': 200,
            'message': 'Location updated successfully',
        } 
    raise HTTPException(status_code=404, detail="Location not found")

@router.delete('/location{id}')
async def delete_location_by_id(id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await delete_location(id)
    if response:
        return "Succesfully deleted"
    raise HTTPException(status_code=204, detail="Location not found")
