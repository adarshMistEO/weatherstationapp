from pydantic import BaseModel,  EmailStr

class User(BaseModel):
    id: int
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


