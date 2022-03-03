from typing import Any, ClassVar, Generic, Type, TypeVar

from server.database.tables import Base
from server.exceptions.repository_exceptions import EntityNotFoundException
from server.middleware.database import db

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    table: ClassVar[Type[T]]

    @classmethod
    async def create(cls, **kwargs) -> T:
        """
        Create a new instance of the model associated with the repository using the specified keyword arguments. This
        method may be overridden in subclasses to provide more verbose parameters.
        """
        db.get().add(model := cls.table(**kwargs))
        await db.get().flush()
        return model

    @classmethod
    async def delete(cls, *models: T) -> None:
        """
        Delete the specified instances of the model associated with the repository.
        """
        for model in models:
            if not isinstance(model, cls.table):
                raise TypeError(f"Expected {cls.table.__name__} instance, got {type(model).__name__}")
        for model in models:
            await db.get().delete(model)
        await db.get().flush()

    @classmethod
    async def get(cls, key: Any, *, raise_if_none=False) -> T | None:
        """
        Get an instance of the model associated with the repository using the specified primary key.
        """
        result = await db.get().get(cls.table, key)
        if raise_if_none and result is None:
            raise EntityNotFoundException(f"{cls.table.__name__} not found for {key=}")
        return result
