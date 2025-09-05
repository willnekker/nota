from pydantic import BaseModel
from datetime import datetime


class CourseBase(BaseModel):
    name: str
    course_code: str
    start_at: datetime | None = None
    end_at: datetime | None = None


class CourseCreate(CourseBase):
    id: int


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True