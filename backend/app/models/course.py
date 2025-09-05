from sqlalchemy import Column, Integer, String, DateTime

from app.db.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    course_code = Column(String)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
