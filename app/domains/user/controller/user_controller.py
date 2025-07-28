from datetime import datetime

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.domains.storage.service.storage_service import StorageService
from app.domains.user.service.user_service import UserService
from app.utils.jwt import decode_access_token
from database.session import get_db

router = APIRouter()

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    today = datetime.today()
    storage_service = StorageService(db)
    token = decode_access_token()

