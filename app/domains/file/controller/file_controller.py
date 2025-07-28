from fastapi import APIRouter, UploadFile
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.utils.jwt import get_current_user
from database.models.file import File
from database.session import get_db

router = APIRouter()

@router.post("/upload")
def upload_file(
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
        current_user: str = Depends(get_current_user)
    ):

