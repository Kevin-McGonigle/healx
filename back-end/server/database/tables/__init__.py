from inflection import tableize
from sqlalchemy.orm import declarative_base, declared_attr


class __Base:
    @declared_attr
    def __tablename__(cls):
        return tableize(cls.__name__)

    @declared_attr
    def __mapper_args__(cls):
        return {"eager_defaults": True}

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}


Base = declarative_base(cls=__Base)
