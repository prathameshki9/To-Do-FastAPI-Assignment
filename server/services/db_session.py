from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

URL: str | None = os.getenv("POSTGRES_SQL_URL")

if URL is None:
    raise ValueError("postgres sql url is missing in environment")

engine = create_engine(URL)

session = sessionmaker(bind=engine)

def create_session():
    db = session()
    try:
        yield db
    finally:
        db.close()