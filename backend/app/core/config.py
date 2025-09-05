from pydantic import BaseSettings


class Settings(BaseSettings):
    CANVAS_API_URL: str = "https://canvas.instructure.com"
    CANVAS_CLIENT_ID: str
    CANVAS_CLIENT_SECRET: str
    CANVAS_REDIRECT_URI: str
    DOWNLOAD_DIR: str = "./downloads"

    class Config:
        env_file = ".env"


settings = Settings()