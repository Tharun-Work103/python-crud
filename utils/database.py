from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    "mysql+pymysql://root:Tharun%401507@localhost/python_crud"
)

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind=engine
)

Base=declarative_base()