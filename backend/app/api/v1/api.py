from fastapi import APIRouter

from app.api.v1 import auth, courses, assignments, announcements, pages, files, summaries

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])
api_router.include_router(assignments.router, prefix="/assignments", tags=["assignments"])
api_router.include_router(announcements.router, prefix="/announcements", tags=["announcements"])
api_router.include_router(pages.router, prefix="/pages", tags=["pages"])
api_router.include_router(files.router, prefix="/files", tags=["files"])
api_router.include_router(summaries.router, prefix="/summaries", tags=["summaries"])