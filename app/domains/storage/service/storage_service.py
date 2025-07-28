import uuid
from datetime import datetime

from app.domains.storage.repository.storage_repository import StorageRepository


class StorageService:
    def __init__(self, db):
        self.storage_repository = StorageRepository(db)

    def get_storage_usage(self, user_id: uuid.UUID, period: datetime):
        return self.storage_repository.get_storage_usage(user_id, period)

    def create_storage_usage(self, user_id: uuid.UUID, period: datetime, used_space: int):
        return self.storage_repository.create_storage_usage(user_id, period, used_space)

    def update_storage_usage(self, user_id: uuid.UUID, period: datetime, used_space: int):
        return self.storage_repository.update_storage_usage(user_id, period, used_space)
