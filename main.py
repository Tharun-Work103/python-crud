from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from utils import models,crud

from utils.database import (
    engine,
    SessionLocal
)

from utils.schemas import UserCreate, UserResponse

models.Base.metadata.create_all(
    bind=engine
)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

@app.post(
    "/users",
    response_model = UserResponse
)

def create_user(
    user:UserCreate,
    db:Session=Depends(get_db)
):
    return crud.create_user(
        db,
        user
    )

@app.get(
    "/users",
    response_model=list[UserResponse]
)

def get_users(
    db:Session=Depends(get_db)
):
    return crud.get_users(db)

@app.put(
    "/users/{id}"
)

def update_user(
    id:int,
    user:UserCreate,
    db:Session=Depends(get_db)
):

    return crud.update_user(
        db,
        id,
        user
    )

@app.delete(
    "/users/{id}"
)
def delete_user(
    id:int,
    db:Session=Depends(get_db)
):
    return crud.delete_user(
        db,
        id
    )