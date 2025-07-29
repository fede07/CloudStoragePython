from fastapi import FastAPI

from app.domains.auth.controller import auth_controller
from app.domains.user.controller import user_controller

# print("Creating database tables...")
# Base.metadata.create_all(bind=engine)
# print("Tables created successfully.")
app = FastAPI()

app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
app.include_router(user_controller.router, prefix="/user", tags=["user"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
