from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.users.models import Base
from src.users.routes import router as user_router
from src.constants import version

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


app = FastAPI(title = "Rest api service", description = "Rest api service", version = version)

# app.include_router(user_router)
@app.on_event("startup") 
async def on_startup(): 
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.create_all) 

app.include_router(user_router)
