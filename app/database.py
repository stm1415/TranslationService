import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv() # loads environment variables from the .env file

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL) #engine is responsible for managing the connection pool and database interactions

SessionLocal = sessionmaker(outocommit=False, autoflush=False, bind=engine)