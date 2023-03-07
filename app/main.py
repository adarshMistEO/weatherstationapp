from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import login, user, weather, location


app = FastAPI()

origins = ['https://localhost:3000']

# Add middleware for Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up routers
app.include_router(login.router, tags=["Log in"])
app.include_router(user.router, tags=["User"])
app.include_router(weather.router, tags=["Weather"])
app.include_router(location.router, tags=["Location"])
