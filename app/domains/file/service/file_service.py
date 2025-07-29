import uuid

from app.domains.file.repository.file_repository import FileRepository
from app.domains.storage.repository.storage_repository import StorageRepository
from fastapi import File as UploadedFile, HTTPException

from app.utils.config import settings
from app.utils.constants import HTTP_STATUS


class FileService:
    def __init__(self, db):
        self.db = db
        self.storage_repository = StorageRepository(db)
        self.file_repository = FileRepository(db)

    def create_file(self, file: UploadedFile , user_id: uuid.UUID):
        content = file.file.read()
        file_size = len(content)
        file_name = file.filename
        storage_usage = self.storage_repository.get_storage_usage(user_id, file.created_at)
        if storage_usage.used_space + file_size > settings.STORAGE_LIMIT:
            storage_exception = HTTPException(
                status_code=HTTP_STATUS.CONFLICT,
                detail="Storage limit exceeded"
            )
            raise storage_exception
        try:
            created_file = self.file_repository.create_file(file_name, file_size, user_id)
            self.storage_repository.update_storage_usage(user_id, created_file.created_at, file_size)
            return created_file
        except Exception:
            raise Exception
        finally:
            file.file.close()
