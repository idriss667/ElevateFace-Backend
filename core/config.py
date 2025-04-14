from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    STRIPE_API_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
