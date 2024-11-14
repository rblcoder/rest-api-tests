from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int
