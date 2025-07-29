from datetime import datetime

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.domains.storage.service.storage_service import StorageService
from app.domains.user.schema.user_schema import UserOut
from app.domains.user.service.user_service import UserService
from app.utils.jwt import get_current_user
from database.session import get_db

router = APIRouter()

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    today = datetime.today()
    storage_service = StorageService(db)

@router.get("/me", response_model = UserOut)
def get_current_user(user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
