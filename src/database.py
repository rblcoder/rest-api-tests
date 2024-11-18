from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import Settings

# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = Settings().DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
