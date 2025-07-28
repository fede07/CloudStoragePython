from datetime import datetime

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from database.models.file import File
from database.models.user import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, username: str, password: str):
        user = User(
            username=username,
            hashed_password=password
        )
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except SQLAlchemyError:
            self.db.rollback()

    def is_admin(self, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        return user.isAdmin

    def get_user_storage_usage(self, username: str, start_time: datetime, end_time: datetime):
        used_space = self.db.query(func.sum(File.size)).filter(
            File.user_id == username,
            File.created_at >= start_time,
            File.created_at <= end_time
        ).scalar() or 0
        return used_space

