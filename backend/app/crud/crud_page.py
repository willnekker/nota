from sqlalchemy.orm import Session

from app.models.page import Page
from app.schemas.page import PageCreate


def get_page(db: Session, page_id: str):
    return db.query(Page).filter(Page.page_id == page_id).first()


def get_pages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Page).offset(skip).limit(limit).all()


def create_page(db: Session, page: PageCreate):
    db_page = Page(**page.dict())
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page