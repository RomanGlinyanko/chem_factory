from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from .config import settings 

DATABASE_URL = settings.database_url_asyncpg
engine = create_async_engine(DATABASE_URL, echo = True)
async_session_maker = async_sessionmaker(engine, class_ = AsyncSession, expire_on_commit = False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

