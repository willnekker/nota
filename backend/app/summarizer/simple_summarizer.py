from .base import Summarizer


class SimpleSummarizer(Summarizer):
    async def summarize(self, text: str) -> str:
        sentences = text.split(". ")
        return ". ".join(sentences[:3]) + "."
