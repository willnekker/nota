from sqlalchemy.orm import Session

from app.models.file import File
from app.schemas.file import FileCreate


def get_file(db: Session, file_id: int):
    return db.query(File).filter(File.id == file_id).first()


def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(File).offset(skip).limit(limit).all()


def create_file(db: Session, file: FileCreate):
    db_file = File(**file.dict())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
