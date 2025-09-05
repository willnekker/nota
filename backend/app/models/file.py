from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    display_name = Column(String)
    content_type = Column(String)
    url = Column(String)
    size = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course")
