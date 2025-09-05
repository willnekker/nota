import httpx
from fastapi import Depends
from sqlalchemy.orm import Session
import os
import re

from app import models
from app.api.deps import get_current_user, get_db
from app.core.config import settings


class CanvasClient:
    def __init__(self, current_user: models.user.User = Depends(get_current_user)):
        self.current_user = current_user
        self.access_token = self.current_user.tokens[-1].access_token
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

    async def _fetch_paginated_data(self, url: str):
        all_data = []
        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
                all_data.extend(response.json())

                # Extract next page URL from Link header
                next_url = None
                if "Link" in response.headers:
                    links = response.headers["Link"].split(",")
                    for link in links:
                        match = re.search(r'<(.+)>; rel="next"', link)
                        if match:
                            next_url = match.group(1)
                            break
                url = next_url
        return all_data

    async def get_courses(self):
        url = f"{settings.CANVAS_API_URL}/api/v1/courses"
        return await self._fetch_paginated_data(url)

    async def get_assignments(self, course_id: int):
        url = f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/assignments"
        return await self._fetch_paginated_data(url)

    async def get_announcements(self, course_id: int):
        url = f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/discussion_topics?only_announcements=true"
        return await self._fetch_paginated_data(url)

    async def get_pages(self, course_id: int):
        url = f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/pages"
        return await self._fetch_paginated_data(url)

    async def get_files(self, course_id: int):
        url = f"{settings.CANVAS_API_URL}/api/v1/courses/{course_id}/files"
        return await self._fetch_paginated_data(url)

    async def download_file(self, file_url: str, filename: str):
        os.makedirs(settings.DOWNLOAD_DIR, exist_ok=True)
        file_path = os.path.join(settings.DOWNLOAD_DIR, filename)
        async with httpx.AsyncClient() as client:
            response = await client.get(file_url, headers=self.headers)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path