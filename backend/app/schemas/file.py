from pydantic import BaseModel
from datetime import datetime


class FileBase(BaseModel):
    filename: str
    display_name: str | None = None
    content_type: str | None = None
    url: str
    size: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    course_id: int


class FileCreate(FileBase):
    id: int


class File(FileBase):
    id: int

    class Config:
        orm_mode = True
