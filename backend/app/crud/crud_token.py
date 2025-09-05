from sqlalchemy.orm import Session

from app.models.token import Token
from app.schemas.token import TokenCreate


def get_token(db: Session, token_id: int):
    return db.query(Token).filter(Token.id == token_id).first()


def get_tokens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Token).offset(skip).limit(limit).all()


def create_token(db: Session, token: TokenCreate):
    db_token = Token(**token.dict())
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token
