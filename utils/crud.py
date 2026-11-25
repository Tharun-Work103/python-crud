from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate

def create_user(
        db:Session,
        user:UserCreate
):
    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_users(db:Session):
    return db.query(User).all()

def get_user(db:Session, user_id:int):
    return(
        db.query(User).filter(User.id == user_id).first()
    )

def update_user(
        db:Session,
        user_id:int,
        user:UserCreate
):
    existing = get_user(
        db,
        user_id
    )

    if existing:
        existing.name = user.name
        existing.email = user.email
        db.commit()
        db.refresh(existing)
    return existing


def delete_user(
        db:Session,
        user_id:int
):
    user=get_user(
        db,
        user_id
    )

    if user:
        db.delete(user)
        db.commit()
    return user