from pydantic import BaseModel
from datetime import datetime


class PageBase(BaseModel):
    title: str
    body: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    course_id: int


class PageCreate(PageBase):
    page_id: str


class Page(PageBase):
    page_id: str

    class Config:
        orm_mode = True