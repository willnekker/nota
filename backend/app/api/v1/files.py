from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db
from app.canvas_api.client import CanvasClient
from app.video_processor import is_video, process_video

router = APIRouter()


@router.post("/sync/{course_id}")
async def sync_files(
    course_id: int,
    db: Session = Depends(get_db),
    canvas_client: CanvasClient = Depends(CanvasClient),
):
    files = await canvas_client.get_files(course_id)
    for file in files:
        db_file = crud.crud_file.get_file(db, file_id=file["id"])
        if not db_file:
            crud.crud_file.create_file(
                db,
                schemas.file.FileCreate(
                    id=file["id"],
                    filename=file["filename"],
                    display_name=file.get("display_name"),
                    content_type=file.get("content-type"),
                    url=file["url"],
                    size=file["size"],
                    created_at=file.get("created_at"),
                    updated_at=file.get("updated_at"),
                    course_id=course_id,
                ),
            )
            # Download the file
            file_path = await canvas_client.download_file(file["url"], file["filename"])

            # Process video files
            if is_video(file.get("content-type", "")):
                transcription = await process_video(file_path)
                print(f"Transcription for {file["filename"]}: {transcription}")

    return {"status": "success"}
