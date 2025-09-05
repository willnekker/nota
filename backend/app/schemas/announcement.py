from pydantic import BaseModel
from datetime import datetime


class AnnouncementBase(BaseModel):
    title: str
    message: str | None = None
    posted_at: datetime | None = None
    course_id: int


class AnnouncementCreate(AnnouncementBase):
    id: int


class Announcement(AnnouncementBase):
    id: int

    class Config:
        orm_mode = True
