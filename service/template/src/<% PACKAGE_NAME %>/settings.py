"""Settings read from the environment, with defaults for local work."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration for <% PROJECT_NAME %>."""

    model_config = SettingsConfigDict(env_file=".env")

    host: str = "127.0.0.1"
    port: int = <% SERVICE_PORT %>
