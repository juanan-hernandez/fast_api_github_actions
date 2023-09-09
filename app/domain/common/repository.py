import abc
from collections.abc import Iterator
from typing import TypeVar, Generic, Any

from app.domain.common.model import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepo(Generic[ModelType], abc.ABC):
    @abc.abstractmethod
    def get(self, *args: Any, **kwargs: Any) -> ModelType:
        raise NotImplementedError

    def get_all(self, *args: Any, **kwargs: Any) -> Iterator[ModelType]:
        raise NotImplementedError

    def add(self, entity: ModelType) -> None:
        raise NotImplementedError
