#Material repository
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Mat

class MatRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, mat_id: int) -> Mat | None:
        query = select(Mat).where(Mat.id == mat_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()