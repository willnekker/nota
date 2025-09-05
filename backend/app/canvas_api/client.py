import httpx
from fastapi import Depends
from sqlalchemy.orm import Session
import os

from app import models
from app.api.deps import get_current_user, get_db
from app.core.config import settings


class CanvasClient:
    def __init__(self, current_user: models.user.User = Depends(get_current_user)):
        self.current_user = current_user
        self.access_token = self.current_user.tokens[-1].access_token
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

    async def get_courses(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.CANVAS_API_URL}/api/v1/courses", headers=self.headers
            )
        response.raise_for_status()
        return response.json()

    async def get_assignments(self, course_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/assignments",
                headers=self.headers,
            )
        response.raise_for_status()
        return response.json()

    async def get_announcements(self, course_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/discussion_topics?only_announcements=true",
                headers=self.headers,
            )
        response.raise_for_status()
        return response.json()

    async def get_pages(self, course_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/pages",
                headers=self.headers,
            )
        response.raise_for_status()
        return response.json()

    async def get_files(self, course_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/files",
                headers=self.headers,
            )
        response.raise_for_status()
        return response.json()

    async def download_file(self, file_url: str, filename: str):
        os.makedirs(settings.DOWNLOAD_DIR, exist_ok=True)
        file_path = os.path.join(settings.DOWNLOAD_DIR, filename)
        async with httpx.AsyncClient() as client:
            response = await client.get(file_url, headers=self.headers)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
