from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from .config import settings 

DATABASE_URL = settings.database_url_asyncpg #Строка (url) для подключеения
#print(f"Connecting to: {DATABASE_URL}") # Посмотрите, что там в консоли

engine = create_async_engine(DATABASE_URL, echo = True) #Движок
async_session_maker = async_sessionmaker(engine, class_ = AsyncSession, expire_on_commit = False)

#Генератор сессий
#Используется в route
#Передается из route в service
#Передается из service в repository
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

