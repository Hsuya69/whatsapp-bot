from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

ASYNC_DB_URL = "mysql+aiomysql://root:Ayush123@localhost:3306/ayuprj"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# For Alembic (Sync)
SYNC_DB_URL = "mysql+pymysql://root:Ayush123@localhost:3306/ayuprj"
sync_engine = create_engine(SYNC_DB_URL, echo=True)
