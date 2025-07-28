import uuid

from app.domains.file.repository.file_repository import FileRepository
from app.domains.storage.repository.storage_repository import StorageRepository
from fastapi import File as UploadedFile

class FileService:
    def __init__(self, db):
        self.db = db
        self.storage_repository = StorageRepository(db)
        self.file_repository = FileRepository(db)

    def create_file(self, file: UploadedFile , user_id: uuid.UUID):
        content = file.file.read()
        file_size = len(content)
        file_name = file.filename
        try:
            created_file = self.file_repository.create_file(file_name, file_size, user_id)
            return created_file
        except Exception:
            raise Exception
        finally:
            file.file.close()
