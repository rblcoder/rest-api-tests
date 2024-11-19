from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


# https://stackoverflow.com/questions/68360687/sqlalchemy-asyncio-orm-how-to-query-the-database
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = Config.DATABASE_URL
engine = create_async_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
