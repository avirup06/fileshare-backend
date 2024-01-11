import urllib.parse
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# from fileshare.settings import get_db_config
from fileshare.settings import get_settings

# DATABASE_URL = None

if os.environ.get('stage'):
    conf = get_settings()

    username = conf.DB_USERNAME
    password = conf.DB_PASSWORD
    host = conf.DB_HOST
    port = conf.DB_PORT
    database_name = conf.DB_NAME
    encoded_password = urllib.parse.quote(password)

    DATABASE_URL: str = f"postgresql+psycopg2://{username}:{encoded_password}@{host}:{port}/{database_name}"


# conf = get_db_config()
# username = conf.USERNAME
# password = conf.PASSWORD
# host = conf.HOST
# port = conf.PORT
# database_name = conf.NAME
# encoded_password = urllib.parse.quote(password)

# DATABASE_URL: str = f"postgresql+psycopg2://{username}:{encoded_password}@{host}:{port}/{database_name}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()