from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.summarizer import SimpleSummarizer, Summarizer

router = APIRouter()


class SummarizeRequest(BaseModel):
    text: str


@router.post("/summarize")
async def summarize_text(
    request: SummarizeRequest,
    summarizer: Summarizer = Depends(SimpleSummarizer),
):
    summary = await summarizer.summarize(request.text)
    return {"summary": summary}
