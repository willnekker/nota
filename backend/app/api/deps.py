from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models
from app.db.base import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db)) -> models.user.User:
    user = crud.crud_user.get_user(db, user_id=1)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
