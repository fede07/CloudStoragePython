from fastapi import HTTPException

from app.domains.user.repository.user_repository import UserRepository
from app.domains.user.user_schema import TokenResponse
from app.utils.jwt import create_access_token
from app.utils.security import Security
from database.models.user import User


class AuthService:
    def __init__(self, db):
        self.db = db
        self.user_repository = UserRepository(db)
        self.security = Security()

    def login(self, username: str, password: str):
        user = self.user_repository.get_user(username)
        if user is None or not self.security.verify_password(password, user.password):
            raise HTTPException(status_code=404, detail="Invalid username or password")
        token = create_access_token({"sub": user.username})
        return TokenResponse(access_token=token)

    def register(self, username: str, password: str):
        user = self.user_repository.get_user(username)
        if user is not None:
            raise HTTPException(status_code=400, detail="Username already registered")
        hashed_password = self.security.get_password_hash(password)
        self.user_repository.create_user(username, hashed_password)
        token = create_access_token({"sub": username})
        return TokenResponse(access_token=token)
