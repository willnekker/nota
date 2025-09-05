from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db
from app.canvas_api.client import CanvasClient

router = APIRouter()


@router.post("/sync/{course_id}")
async def sync_assignments(
    course_id: int,
    db: Session = Depends(get_db),
    canvas_client: CanvasClient = Depends(CanvasClient),
):
    assignments = await canvas_client.get_assignments(course_id)
    for assignment in assignments:
        db_assignment = crud.crud_assignment.get_assignment(
            db, assignment_id=assignment["id"]
        )
        if not db_assignment:
            crud.crud_assignment.create_assignment(
                db,
                schemas.assignment.AssignmentCreate(
                    id=assignment["id"],
                    name=assignment["name"],
                    description=assignment.get("description"),
                    due_at=assignment.get("due_at"),
                    course_id=course_id,
                ),
            )
    return {"status": "success"}
