from typing import List

from server.database.tables.documents import Document
from server.repositories.document_repository import DocumentRepository


async def get_reading_list() -> List[Document]:
    return await DocumentRepository.get_reading_list()


async def set_document_reading_list(document_id: int, value: bool) -> None:
    (await DocumentRepository.get(document_id)).reading_list = value
