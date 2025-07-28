import uuid

from database.models.file import File
from sqlalchemy.exc import SQLAlchemyError

class FileRepository:
    def __init__(self, db):
        self.db = db

    def create_file(self, file_name: str, file_size: int, user_id: uuid.UUID):
        file_entry = File(
            filename=file_name,
            size=file_size,
            user_id=user_id
        )
        try:
            self.db.add(file_entry)
            self.db.commit()
            self.db.refresh(file_entry)
        except (SQLAlchemyError, ValueError):
            self.db.rollback()
