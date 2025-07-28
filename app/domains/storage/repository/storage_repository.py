import uuid
from datetime import datetime

from database.models.storage_usage import StorageUsage
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

class StorageRepository:
    def __init__(self, db):
        self.db = db

    def get_storage_usage(self, user_id: uuid.UUID, period: datetime) -> StorageUsage:
        period_date = period.date()
        return self.db.query(StorageUsage).filter(
            StorageUsage.user_id == user_id,
            StorageUsage.period == period_date
        ).first()

    def create_storage_usage(self, user_id: uuid.UUID, period: datetime, used_space: int) -> StorageUsage:
        storage_usage = StorageUsage(
            user_id=user_id,
            period=period.date(),
            used_space=used_space
        )
        try:
            self.db.add(storage_usage)
            self.db.commit()
            self.db.refresh(storage_usage)
            return storage_usage
        except SQLAlchemyError:
            self.db.rollback()
            raise Exception

    def update_storage_usage(self, user_id: uuid.UUID, period: datetime, used_space: int) -> StorageUsage:
        period_date = period.date()
        old_storage_usage = self.db.query(StorageUsage).filter(
            StorageUsage.user_id == user_id,
            StorageUsage.period == period_date
        ).first()
        if old_storage_usage is None:
            try:
                return self.create_storage_usage(user_id, period, used_space)
            except IntegrityError:
                raise Exception
        else:
            try:
                old_storage_usage.used_space += used_space
                self.db.commit()
                self.db.refresh(old_storage_usage)
                return old_storage_usage
            except SQLAlchemyError:
                self.db.rollback()
                raise Exception
