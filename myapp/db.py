from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlalchemy import create_engine


ASYNC_DB_URL = "postgresql+asyncpg://postgres:Ayush123@localhost:5432/mybot"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# For Alembic (Sync)
SYNC_DB_URL = "postgresql+psycopg2://postgres:Ayush123@localhost:5432/mybot"
sync_engine = create_engine(SYNC_DB_URL, echo=True)
