import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, DateTime, UUID
from sqlalchemy.orm import relationship
from database.session import Base


class File(Base):
    __tablename__ = 'files'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    size = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    user = relationship("User", back_populates="files")
