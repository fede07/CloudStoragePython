import sqlalchemy.exc
from fastapi import FastAPI

from database.session import engine, Base
from routes import auth

print("Creating database tables...")
try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
except sqlalchemy.exc.OperationalError:
    print("Tables already exist.")
app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
