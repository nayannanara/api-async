from typing import Optional
from sqlmodel import Field, SQLModel


class Curso(SQLModel, table=True):
    __tablename__  = 'cursos'

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int 