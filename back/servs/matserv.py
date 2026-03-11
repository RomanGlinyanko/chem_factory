#matserv.py
from sqlalchemy.ext.asyncio import AsyncSession
from ..repos.matrepo import MatRepository #Основной класс из репо
from ..schemas import MatResponce #Класс ответа из схем

class MatService:
    def __init__(self, session: AsyncSession):
        self.repository = MatRepository(session)

    async def get_material(self, mat_id: int) -> MatResponce | None:
        mat_model = await self.repository.get_by_id(mat_id) #Вызов репозитория
        
        if not mat_model:return None
            
        # Превращаем модель SQLAlchemy в Pydantic схему
        # Присваивает полям класса ответа из схем значения
        return MatResponce(
            id = mat_model.id,
            name = mat_model.name or "Без названия"
        )
