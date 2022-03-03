from typing import List

from fastapi import APIRouter, Path

from server.models.document import Document
from server.models.enum.search_method import SearchMethod
from server.services import search_service

router = APIRouter(prefix="/search")


@router.get("/{query}")
async def search(
    query: str = Path(..., max_length=100),
    method: SearchMethod = SearchMethod.keyword,
    limit: int = None
) -> List[Document]:
    return [Document(**d.to_dict()) for d in (await search_service.search(query, method, limit))]
