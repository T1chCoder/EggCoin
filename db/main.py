import config
from db import actions
from db.models import main, event_listeners, validators
import sqlmodel as sql
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(config.DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(sql.SQLModel.metadata.create_all)
        actions.log_info("Database connected successfully and is now running")
    except Exception as e:
        actions.log_error(e)

