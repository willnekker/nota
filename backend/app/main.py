from fastapi import FastAPI

from app.api.v1.api import api_router
from app.db.base import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"Hello": "World"}
