from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Page(Base):
    __tablename__ = "pages"

    page_id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course")