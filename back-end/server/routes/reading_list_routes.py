from typing import List

from fastapi import APIRouter

from server.models.document import Document
from server.services import reading_list_service

router = APIRouter(prefix="/reading-list")


@router.post("/{document_id}")
async def add_document_to_reading_list(document_id: int) -> None:
    await reading_list_service.set_document_reading_list(document_id, True)


@router.get("/")
async def get_reading_list() -> List[Document]:
    return [Document(**d.to_dict()) for d in (await reading_list_service.get_reading_list())]


@router.delete("/{document_id}")
async def remove_document_from_reading_list(document_id: int) -> None:
    await reading_list_service.set_document_reading_list(document_id, False)
