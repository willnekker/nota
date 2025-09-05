import os
import whisper
from app.core.config import settings

def is_video(content_type: str) -> bool:
    return content_type.startswith("video/")


async def process_video(file_path: str):
    # TODO: Research Canvas API for fetching captions for videos.
    # This might involve checking if the video has associated text tracks or external caption files.
    captions_available = False  # Placeholder: Assume no captions for now

    if captions_available:
        print(f"Captions available for {file_path}. Fetching...")
        # Logic to fetch captions from Canvas API or associated files
        return "Captions fetched"
    else:
        print(f"No captions for {file_path}. Transcribing audio...")
        # Ensure the Whisper model is loaded. For production, consider loading it once globally.
        model = whisper.load_model("base")
        result = model.transcribe(file_path)
        return result["text"]