from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin:123qweasdzxc@localhost:5432/taperav1"
DB_DRIVER = os.getenv("DB_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_POOL_SIZE = os.getenv("DB_POOL_SIZE")
DB_DIALECT = DB_DRIVER + "+psycopg2"  
SQLALCHEMY_DATABASE_URL = '%s://%s:%s@%s:%s/%s' % (
    DB_DIALECT, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()