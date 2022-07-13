from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "postgresql+asyncpg://postgres:admin2255@localhost:5433/fcms"
engine = create_async_engine(DB_URL, future=True, echo=True)
AsynSessionFactory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()