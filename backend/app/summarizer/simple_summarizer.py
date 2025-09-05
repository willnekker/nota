from .base import Summarizer


class SimpleSummarizer(Summarizer):
    async def summarize(self, text: str) -> str:
        # This is a very basic summarizer. For more advanced summarization,
        # you can integrate with various LLMs (e.g., OpenAI, Hugging Face models).
        # This modular interface allows easy swapping of different summarization implementations.
        sentences = text.split(". ")
        return ". ".join(sentences[:3]) + "."