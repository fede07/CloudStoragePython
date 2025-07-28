import uuid

from sqlalchemy import BigInteger, Date, UUID, Column, UniqueConstraint
from sqlalchemy.orm import relationship

from database.session import Base


class StorageUsage(Base):
    __tablename__ = 'storage_usage'

    id = Column(UUID(as_uuid=True), index=True, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True) , index=True)
    period = Column(Date, nullable=False)
    used_space = Column(BigInteger, nullable=False, default=0)

    user = relationship("User", back_populates="storage_usage")

    __table_args__ = (UniqueConstraint('user_id', 'period', name='_user_period_uc'),)

