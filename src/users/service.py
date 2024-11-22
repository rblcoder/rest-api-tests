from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from src.users.models import User
from src.users.schema import UserCreate

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate):
        db_user = User(name=user.name, email=user.email)
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def read_users(self, skip: int = 0, limit: int = 10):
        result = await self.db.scalars(select(User).offset(skip).limit(limit))
        return result.all()

    async def read_user(self, user_id: int):
        result = await self.db.scalars(select(User).filter(User.id == user_id))
        return result.first()

    async def update_user(self, user_id: int, user: UserCreate):
        result = await self.db.scalars(select(User).filter(User.id == user_id))
        db_user = result.first()
        if db_user is None:
            return None
        db_user.name = user.name
        db_user.email = user.email
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def delete_user(self, user_id: int):
        result = await self.db.scalars(select(User).filter(User.id == user_id))
        db_user = result.first()
        if db_user is None:
            return None
        await self.db.delete(db_user)
        await self.db.commit()
        return db_user
