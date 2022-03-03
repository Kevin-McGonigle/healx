import re
from typing import List

from server.database.tables.documents import Document
from server.models.enum.search_method import SearchMethod
from server.repositories.document_repository import DocumentRepository


async def search(query: str, method: SearchMethod, limit: int | None) -> List[Document]:
    match method:
        case SearchMethod.bm25:
            return (await bm25_search(query))[:limit]
        case SearchMethod.keyword:
            return (await keyword_search(query))[:limit]
        case SearchMethod.regex:
            return (await regex_search(query))[:limit]
        case SearchMethod.tf_idf:
            return (await tf_idf_search(query))[:limit]
        case _:
            raise


async def bm25_search(_: str) -> List[Document]:
    """
    Search the title, abstract and authors using the Okapi BM25 ranking function.
    """
    raise NotImplementedError


async def keyword_search(query: str) -> List[Document]:
    """
    Search the title, abstract and authors for each term in the query, sorting by the sum of frequencies of each term.
    """
    results = await regex_search(fr"\b({query.replace(' ', '|')})\b")
    return results


async def regex_search(query: str) -> List[Document]:
    """
    Search the title, abstract and authors using the specified query as a regex pattern, sorting by frequency.
    """
    results = {}
    async for document in await DocumentRepository.with_text_matching(query):
        if count := get_pattern_count(query, document):
            if count in results:
                results[count].append(document)
            else:
                results[count] = [document]
    return [document for _, v in sorted(results.items(), key=lambda item: item[0], reverse=True) for document in v]


async def tf_idf_search(_: str) -> List[Document]:
    """
    Search the title, abstract and authors using "term frequency-inverse document frequency" (tf-idf) and cosine
    similarity.
    """
    raise NotImplementedError


def get_pattern_count(pattern: str, document: Document):
    """
    Get the total number of matches of the specified pattern in the specified document's authors, title and abstract.
    """
    return ((len(re.findall(pattern, document.authors)) if document.authors else 0)
            + (len(re.findall(pattern, document.title)) if document.title else 0)
            + (len(re.findall(pattern, document.abstract)) if document.abstract else 0))
