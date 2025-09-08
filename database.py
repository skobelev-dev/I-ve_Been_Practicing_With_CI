from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite+aiosqlite:///./main.py.db"

engine = create_async_engine(DATABASE_URL, echo=True)
sync_engine = create_engine('sqlite:///main.py.db')

async_session = async_sessionmaker(engine, expire_on_commit=False)
session = async_session()
Base = declarative_base()
