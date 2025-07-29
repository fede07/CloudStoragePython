from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    is_admin: bool

    class Config:
        from_attributes= True

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
