"""The <% PROJECT_NAME %> web service."""

import uvicorn
from fastapi import FastAPI

from <% PACKAGE_NAME %>.settings import Settings

app = FastAPI(title="<% PROJECT_NAME %>")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the service is up."""
    return {"status": "ok"}


def main() -> None:
    """Run the service with the configured host and port."""
    settings = Settings()
    uvicorn.run(app, host=settings.host, port=settings.port)
