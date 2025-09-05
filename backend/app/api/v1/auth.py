from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
import httpx
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db.base import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/login")
def login():
    return RedirectResponse(
        f"{settings.CANVAS_API_URL}/login/oauth2/auth?"
        f"client_id={settings.CANVAS_CLIENT_ID}&"
        f"response_type=code&"
        f"redirect_uri={settings.CANVAS_REDIRECT_URI}"
    )


@router.get("/callback")
async def callback(request: Request, code: str, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.CANVAS_API_URL}/login/oauth2/token",
            data={
                "client_id": settings.CANVAS_CLIENT_ID,
                "client_secret": settings.CANVAS_CLIENT_SECRET,
                "code": code,
                "redirect_uri": settings.CANVAS_REDIRECT_URI,
                "grant_type": "authorization_code",
            },
        )
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Could not exchange code for token")

    access_token = response.json()["access_token"]

    # Create a dummy user for now
    user = crud.crud_user.create_user(db, user=schemas.user.UserCreate(email="test@example.com", password="test"))

    # Store the token in the database
    crud.crud_token.create_token(db, token=schemas.token.TokenCreate(access_token=access_token, user_id=user.id))

    return {"access_token": access_token}