import os
import whisper

from app.core.config import settings

def is_video(content_type: str) -> bool:
    return content_type.startswith("video/")


async def process_video(file_path: str):
    # Placeholder for fetching captions
    captions_available = False  # Replace with actual logic to check for captions

    if captions_available:
        print(f"Captions available for {file_path}. Fetching...")
        # Logic to fetch captions
        return "Captions fetched"
    else:
        print(f"No captions for {file_path}. Transcribing audio...")
        # Logic to download audio (if not already audio) and transcribe with Whisper
        model = whisper.load_model("base")
        result = model.transcribe(file_path)
        return result["text"]
