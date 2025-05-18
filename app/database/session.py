import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://fastapi_user:password@localhost:5432/fastapi_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

# Dependency for FastAPI
def GetDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()