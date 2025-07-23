from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, UUID, String, Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    isAdmin = Column(Boolean, nullable=False)
