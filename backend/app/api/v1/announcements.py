from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db
from app.canvas_api.client import CanvasClient

router = APIRouter()


@router.post("/sync/{course_id}")
async def sync_announcements(
    course_id: int,
    db: Session = Depends(get_db),
    canvas_client: CanvasClient = Depends(CanvasClient),
):
    announcements = await canvas_client.get_announcements(course_id)
    for announcement in announcements:
        db_announcement = crud.crud_announcement.get_announcement(
            db, announcement_id=announcement["id"]
        )
        if not db_announcement:
            crud.crud_announcement.create_announcement(
                db,
                schemas.announcement.AnnouncementCreate(
                    id=announcement["id"],
                    title=announcement["title"],
                    message=announcement.get("message"),
                    posted_at=announcement.get("posted_at"),
                    course_id=course_id,
                ),
            )
    return {"status": "success"}
