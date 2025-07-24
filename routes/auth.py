from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.models.user import User
from database.session import get_db
from schemas.user.user import TokenResponse, LoginRequest
from utils.jwt import create_access_token
from utils.security import verify_password, get_password_hash, oauth2_scheme, bearer_scheme

router = APIRouter()

@router.post("/login", response_model = TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if user is None or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=404, detail="Invalid username or password")
    token = create_access_token({"sub": user.username})
    return TokenResponse(access_token=token)

@router.post("/register", response_model = TokenResponse)
def register(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if user is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(data.password)
    user = User(
        username=data.username,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    token = create_access_token({"sub": user.username})
    return TokenResponse(access_token=token)

@router.get("/health")
def health(token: str = Depends(bearer_scheme)):
    return {"status": "ok"}
