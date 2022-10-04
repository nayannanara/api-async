from core.configs import settings
from sqlalchemy import Column, Integer, String


class Curso(settings.DBBaseModel):
    __tablename__  = 'cursos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: str = Column(Integer)
    horas: str = Column(Integer)