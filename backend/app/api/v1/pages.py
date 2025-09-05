from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db
from app.canvas_api.client import CanvasClient

router = APIRouter()


@router.post("/sync/{course_id}")
async def sync_pages(
    course_id: int,
    db: Session = Depends(get_db),
    canvas_client: CanvasClient = Depends(CanvasClient),
):
    pages = await canvas_client.get_pages(course_id)
    for page in pages:
        db_page = crud.crud_page.get_page(db, page_id=page["url"])
        if not db_page:
            crud.crud_page.create_page(
                db,
                schemas.page.PageCreate(
                    page_id=page["url"],
                    title=page["title"],
                    body=page.get("body"),
                    created_at=page.get("created_at"),
                    updated_at=page.get("updated_at"),
                    course_id=course_id,
                ),
            )
    return {"status": "success"}