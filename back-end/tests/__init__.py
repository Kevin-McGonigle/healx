from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from server.middleware.database import db


@asynccontextmanager
async def db_session(engine: AsyncEngine = None):
    try:
        if not engine:
            engine = create_async_engine("sqlite+aiosqlite:///:memory:", pool_recycle=3600)
        async with AsyncSession(engine) as session:
            async with session.begin():
                db.set(session)
                yield
    except Exception:
        raise
