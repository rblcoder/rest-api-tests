from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.database import SessionLocal

from src.users.schema import UserCreate, UserResponse
from src.users.service import UserService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    db_user = await user_service.create_user(user)
    return db_user

@router.get("/", response_model=List[UserResponse])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    users = await user_service.read_users(skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    db_user = await user_service.read_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    db_user = await user_service.update_user(user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    db_user = await user_service.delete_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
