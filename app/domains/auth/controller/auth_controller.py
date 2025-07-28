from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.domains.auth.service.auth_service import AuthService
from app.utils.security import bearer_scheme
from database.session import get_db
from app.domains.user.schema.user_schema import TokenResponse, LoginRequest

router = APIRouter()

@router.post("/login", response_model = TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.login(data.username, data.password)

@router.post("/register", response_model = TokenResponse)
def register(data: LoginRequest, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.register(data.username, data.password)

@router.get("/health")
def health(token: str = Depends(bearer_scheme)):
    return {"status": "ok"}
