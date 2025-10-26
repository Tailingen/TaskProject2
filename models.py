from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(url="sqlite+aiosqlite:///test.db", echo=True)

class Base(DeclarativeBase):
    pass

#Таблицы

class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    status: Mapped[bool]

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)