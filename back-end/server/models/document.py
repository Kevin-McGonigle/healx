from datetime import date

from pydantic import BaseModel


class Document(BaseModel):
    id: int
    abstract: str | None
    authors: str | None
    doi: str | None
    journal: str | None
    reading_list: bool
    published: date | None
    source: str
    title: str | None
    url: str | None

    class Config:
        orm_mode = True
