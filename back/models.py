#Модели базы данных
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, BigInteger, Text

class Base(DeclarativeBase):
    metadata = MetaData(schema = 'chem_fact')

class Mat(Base):
    __tablename__ = 'mat'
    id: Mapped[int] = mapped_column(BigInteger, primary_key = True)
    name: Mapped[Optional[str]] = mapped_column(Text)
