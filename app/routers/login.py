from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.utils import AuthHandler
from db.database import client, collection_user
from models.login import TokenResponse, LoginRequest
from auth.utils import AuthHandler

router = APIRouter()
auth_handler  = AuthHandler()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.post("/token", response_model=TokenResponse)
async def login(login_request: LoginRequest):
    user = await collection_user.find_one({"email": login_request.username})
    if not user or not auth_handler.verify_password(login_request.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = auth_handler.encode_token(str(user["email"]))
    return TokenResponse(access_token=access_token)

