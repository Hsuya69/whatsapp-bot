from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlalchemy import create_engine


ASYNC_DB_URL = "postgresql+asyncpg://wbotdb_user:9VCtqeI6TpLenPIfAftu3NuRT1yxWsio@dpg-d2g9vuruibrs73e51il0-a.oregon-postgres.render.com/wbotdb"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# For Alembic (Sync)
SYNC_DB_URL = "postgresql+psycopg2://wbotdb_user:9VCtqeI6TpLenPIfAftu3NuRT1yxWsio@dpg-d2g9vuruibrs73e51il0-a.oregon-postgres.render.com/wbotdb"
sync_engine = create_engine(SYNC_DB_URL, echo=True)
