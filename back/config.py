from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    DB_HOST: str = Field(default = "localhost")
    DB_PORT: int = Field(default = 5432)
    DB_USER: str = Field(default = "")
    DB_PASS: str = Field(default = "")
    DB_NAME: str = Field(default = "")

    @property
    def database_url_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file = ".env", env_file_encoding = "utf-8")

settings = Settings()
