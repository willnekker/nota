from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: CourseCreate):
    db_course = Course(id=course.id, name=course.name, course_code=course.course_code, start_at=course.start_at, end_at=course.end_at)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course