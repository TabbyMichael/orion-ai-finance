from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()