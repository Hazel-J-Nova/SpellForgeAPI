from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
password = os.getenv("POSTGRES_PASSWORD")

SQLALCHEMY_DATABASE_URL = f'postgresql://{password}:1234@localhost:5432/spells'


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
