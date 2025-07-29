from datetime import datetime, timedelta

from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.utils.config import settings
from app.utils.security import bearer_scheme


def create_access_token(data: dict, expires_minutes: int = settings.JWT_EXPIRATION_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

def get_username_from_token(token: str):
    payload = decode_access_token(token)
    if payload is None:
        return None
    return payload.get("sub")

def get_current_user(token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username = get_username_from_token(token.credentials)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
