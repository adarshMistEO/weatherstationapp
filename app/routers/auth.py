# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from auth.config import settings
# # from db import get_database, DB_NAME
# from schemas.user import User

# router = APIRouter()

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Authentication scheme
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Token generation
# def create_access_token(data: dict, expires_delta: timedelta):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
#     return encoded_jwt

# # User authentication
# async def authenticate_user(username: str, password: str):
#     db = get_database()[DB_NAME]
#     user = await db.users.find_one({"username": username})
#     if not user:
#         return False
#     if not pwd_context.verify(password, user['password']):
#         return False
#     return user

# # Token endpoint
# @router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = await authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token(
#         data={"sub": user["username"]},
#         expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

# # Current user endpoint
# async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
#     try:
#         payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Invalid authentication credentials",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     db = get_database()[DB_NAME]
#     user = await db.users.find_one({"username": username})
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user

# # Protected endpoint
# @router.get("/protected")
# async def protected_route(current_user: dict = Depends(get_current_user)):
#     return {"message": "You are authenticated"}

