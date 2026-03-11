#Роутеры для операций с материалами
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import MatResponce
from ..servs.matserv import MatService 
from ..database import get_async_session

router = APIRouter()

@router.get('/mat/', response_model = MatResponce) 
#Здесь response_model = MatResponce указывается для фильтрации и валидации типов ответа 
# в соответствию со схемой
async def get_mat(
    id: int, # FastAPI возьмет это из URL id = 5
    session: AsyncSession = Depends(get_async_session) # FastAPI сам создаст сессию
)-> MatResponce: #Аналогично response_model = MatResponce (можно только что-то одно)
    # 1. Создаем сервис, передавая уже готовую сессию
    service = MatService(session)
    # 2. Передаем конкретный ID в метод
    result = await service.get_material(id) #await используется только с async def
    
    if not result:
        raise HTTPException(status_code = 404, detail = f"Материал с id = {id} не найден.")
        
    return result