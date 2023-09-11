import uuid
from typing import TypeVar, Any, Iterator

from pydantic import BaseModel

from app.domain.common.repository import BaseRepo
from app.domain.user.model import User

ModelType = TypeVar("ModelType", bound=BaseModel)


class UserRepositoryInterface(BaseRepo[User]):
    def get(self, user_id: uuid.UUID) -> User:
        raise NotImplementedError

    def get_all(self, *args: Any, **kwargs: Any) -> Iterator[User]:
        raise NotImplementedError

    def add(self, entity: User) -> None:
        raise NotImplementedError
