from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncScalarResult

from server.database.tables.documents import Document
from server.middleware.database import db
from server.repositories.base_repository import BaseRepository


class DocumentRepository(BaseRepository[Document]):
    table = Document

    @classmethod
    async def get_reading_list(cls) -> List[Document]:
        """
        Select rows where reading_list is true.
        """
        return (await db.get().scalars(select(cls.table).where(cls.table.reading_list))).all()

    @classmethod
    async def with_text_matching(cls, pattern: str) -> AsyncScalarResult:
        """
        Select rows for which the pattern matches either the authors, title or abstract, returning a generative stream
        of results.

        Note: While flags are specified, they merely communicate intention. SQLAlchemy with SQLite does not support
        regular expression flags. As a result, matching is case-sensitive. This wouldn't be the case with a more robust
        database such as MySQL or PostgreSQL.
        """
        statement = select(cls.table).where(
            cls.table.title.regexp_match(pattern, "im")
            | cls.table.authors.regexp_match(pattern, "im")
            | cls.table.abstract.regexp_match(pattern, "im")
        )
        return await db.get().stream_scalars(statement)
