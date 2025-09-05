from pydantic import BaseModel
from datetime import datetime


class AssignmentBase(BaseModel):
    name: str
    description: str | None = None
    due_at: datetime | None = None
    course_id: int


class AssignmentCreate(AssignmentBase):
    id: int


class Assignment(AssignmentBase):
    id: int

    class Config:
        orm_mode = True
