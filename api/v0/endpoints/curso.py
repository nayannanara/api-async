from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso import Curso
from schemas.curso import CursoSchema

from core.deps import get_session


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso_in: CursoSchema, db: AsyncSession = Depends(get_session)):
    curso = Curso(titulo=curso_in.titulo, aulas=curso_in.aulas, horas=curso_in.aulas)

    db.add(curso)
    await db.commit()

    return curso


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)) -> CursoSchema:
    cursos: List[CursoSchema] = (await db.execute(select(Curso))).scalars().all()

    return cursos


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=CursoSchema)
async def get_curso(id: int, db: AsyncSession = Depends(get_session)) -> CursoSchema:
    curso =  (await db.execute(select(Curso).filter_by(id=id))).scalars().first()

    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
    return curso
        

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CursoSchema)
async def put_curso(id: int, curso_in: CursoSchema, db: AsyncSession = Depends(get_session)) -> CursoSchema:
    curso =  (await db.execute(select(Curso).filter_by(id=id))).scalars().first()

    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
        
    curso.titulo = curso_in.titulo
    curso.aulas = curso_in.aulas
    curso.horas = curso_in.horas

    await db.commit()

    return curso


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(id: int, db: AsyncSession = Depends(get_session)):
    curso =  (await db.execute(select(Curso).filter_by(id=id))).scalars().first()

    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    await db.delete(curso)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)        