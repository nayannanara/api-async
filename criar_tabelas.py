from core.database import engine

from sqlmodel import SQLModel


async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

    print('tabelas criadas com sucesso')


if __name__ == '__main__'    :
    import asyncio

    asyncio.run(create_tables())