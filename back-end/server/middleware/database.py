from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

db: ContextVar[AsyncSession] = ContextVar("db")


class AsyncDatabaseSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super(AsyncDatabaseSessionMiddleware, self).__init__(app)
        self.engine = create_async_engine("sqlite+aiosqlite:///main.db", echo=True, pool_recycle=3600)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                db.set(session)
                return await call_next(request)
