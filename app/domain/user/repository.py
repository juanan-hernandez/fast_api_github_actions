import uuid
from typing import Any, Iterator

from app.domain.user import UserRepositoryInterface, User


class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection: Any):
        self.db_connection = db_connection

    def get(self, user_id: uuid.UUID) -> User:
        return User(id=user_id, name="Juan", nickname="juanan-hernandez")  # temporary

    def get_all(self, *args: Any, **kwargs: Any) -> Iterator[User]:
        raise NotImplementedError

    def add(self, entity: User) -> None:
        pass
