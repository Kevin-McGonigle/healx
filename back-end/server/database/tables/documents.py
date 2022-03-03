from datetime import date

from sqlalchemy import Boolean, Column, Date, Integer, String, Unicode

from server.database.tables import Base


class Document(Base):
    id: Column | int = Column(Integer, primary_key=True, autoincrement=True)
    abstract: Column | str = Column(Unicode)
    authors: Column | str = Column(Unicode)
    cord_uid: Column | str = Column(String)
    doi: Column | str = Column(String)
    journal: Column | str = Column(Unicode)
    published: Column | date = Column(Date)
    reading_list: Column | bool = Column(Boolean, default=False)
    sha: Column | str = Column(String)
    source: Column | str = Column(String)
    title: Column | str = Column(Unicode)
    url: Column | str = Column(Unicode)
