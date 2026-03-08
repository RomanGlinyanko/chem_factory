from pydantic import BaseModel, Field
from typing import Optional

#Запрос имени материала по id
class MatRequest(BaseModel):
    id:int = Field()

#Ответ - id и название материала
class MatResponce(BaseModel):
    id:int
    name:str