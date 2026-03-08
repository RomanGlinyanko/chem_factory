#Роутеры для операций с материалами
from fastapi import APIRouter

router = APIRouter()

@router.get('/mat/')
async def set_mat():
    return {"message" : "Success"}