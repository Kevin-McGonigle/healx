from dateutil.parser import parse
from pandas import DataFrame, notnull, read_csv, Series
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from server.database.tables import Base
from server.database.tables.documents import Document

engine = create_engine("sqlite:///main.db", echo=True)


def csv_row_to_document(row: Series):
    return Document(
        abstract=row.abstract,
        authors=row.authors,
        cord_uid=row.cord_uid,
        doi=row.doi,
        journal=row.journal,
        published=parse(row.publish_time).date() if row.publish_time else None,
        sha=row.sha,
        source=row.source_x,
        title=row.title,
        url=row.url,
    )


def populate_documents():
    df: DataFrame = read_csv("metadata.csv", dtype=object)
    documents = df.where(notnull(df), None).apply(csv_row_to_document, axis=1).to_list()
    with Session(engine) as session, session.begin():
        session.add_all(documents)


def recreate_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def main():
    recreate_tables()
    populate_documents()


if __name__ == "__main__":
    main()
