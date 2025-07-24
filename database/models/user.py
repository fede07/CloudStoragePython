import uuid
from sqlalchemy import Column, String, Boolean, UUID
from database.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, index=True, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    isAdmin = Column(Boolean, nullable=False, default=False)
