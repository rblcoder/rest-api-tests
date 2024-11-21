from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from src.users.models import Base
from src.users.routes import router as user_router
from src.constants import version

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base.metadata.create_all(bind=engine)


app = FastAPI(title = "Rest api service", description = "Rest api service", version = version)

# # app.include_router(user_router)
# @app.on_event("startup") 
# async def on_startup(): 
#     async with engine.begin() as conn: 
#         await conn.run_sync(Base.metadata.create_all) 


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

app.include_router(user_router)
