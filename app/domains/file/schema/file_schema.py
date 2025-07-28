import uuid
from datetime import datetime


class FileCreate:
    name: str
    size: int
    user_id: uuid.UUID

class FileOut:
    id: int
    name: str
    size: int
    created_at: datetime
    user_id: uuid.UUID
