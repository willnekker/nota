from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api.deps import get_db
from app.canvas_api.client import CanvasClient

router = APIRouter()


@router.post("/sync")
async def sync_courses(
    db: Session = Depends(get_db),
    canvas_client: CanvasClient = Depends(CanvasClient),
):
    courses = await canvas_client.get_courses()
    for course in courses:
        db_course = crud.crud_course.get_course(db, course_id=course["id"])
        if not db_course:
            crud.crud_course.create_course(
                db,
                schemas.course.CourseCreate(
                    id=course["id"],
                    name=course["name"],
                    course_code=course["course_code"],
                    start_at=course.get("start_at"),
                    end_at=course.get("end_at"),
                ),
            )
    return {"status": "success"}


@router.post("/", response_model=schemas.course.Course)
def create_course(course: schemas.course.CourseCreate, db: Session = Depends(get_db)):
    return crud.crud_course.create_course(db=db, course=course)


@router.get("/", response_model=list[schemas.course.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.crud_course.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get("/{course_id}", response_model=schemas.course.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.crud_course.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course