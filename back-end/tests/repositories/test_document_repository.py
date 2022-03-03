from typing import Any, Dict, Iterable, List
from unittest import IsolatedAsyncioTestCase

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from server.database.tables import Base
from server.database.tables.documents import Document
from server.repositories.document_repository import DocumentRepository
from tests import db_session


class TestDocumentRepository(IsolatedAsyncioTestCase):
    @staticmethod
    def documents_to_dicts(documents: Iterable[Document]) -> List[Dict[str, Any]]:
        return [document.to_dict() for document in documents]

    async def asyncSetUp(self) -> None:
        self.engine = create_async_engine("sqlite+aiosqlite:///:memory:", pool_recycle=3600)

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        async with AsyncSession(self.engine) as session:
            async with session.begin():
                session.add_all(
                    [
                        Document(abstract="abstract", authors="authors", title="title"),
                        Document(abstract="foo abstract", authors="foo authors", title=None),
                        Document(abstract="abstract bar", authors=None, title="foo title"),
                        Document(abstract="foo abstract bar", authors=None, title=None),
                        Document(abstract=None, authors="authors bar", title="title bar"),
                        Document(abstract=None, authors="foo authors bar", title=None),
                        Document(abstract=None, authors=None, title="foo title bar"),
                        Document(abstract=None, authors=None, title=None),
                    ]
                )

    async def assert_count_for_pattern(self, pattern, expected_count):
        self.assertEqual(len([d async for d in await DocumentRepository.with_text_matching(pattern)]), expected_count)

    async def test_with_text_matching(self):
        async with db_session(self.engine):
            await self.assert_count_for_pattern(r"\babstract\b", 4)
            await self.assert_count_for_pattern(r"\bauthors\b", 4)
            await self.assert_count_for_pattern(r"\btitle\b", 4)
            await self.assert_count_for_pattern(r"\b(abstract|authors)\b", 6)
            await self.assert_count_for_pattern(r"\b(abstract|title)\b", 6)
            await self.assert_count_for_pattern(r"\b(authors|title)\b", 6)
            await self.assert_count_for_pattern(r"\b(abstract|authors|title)\b", 7)
            await self.assert_count_for_pattern(r"\bsomething else\b", 0)
