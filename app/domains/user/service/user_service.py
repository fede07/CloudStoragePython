import uuid

from app.domains.user.repository.user_repository import UserRepository


class UserService:
    def __init__(self, db):
        self.db = db
        self.user_repository = UserRepository(db)

    def get_user(self, username: str):
        return self.user_repository.get_user(username)
