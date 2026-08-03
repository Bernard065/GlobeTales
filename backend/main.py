"""Backend entry point for the GlobeTales API."""

from fastapi import FastAPI

# Create FastAPI app with metadata
app = FastAPI(
    title="GlobeTales API",
    description="Backend services for the GlobeTales travel and hiking app.",
    version="1.0.0"
)

@app.get("/")
def root() -> dict[str, str]:
    """Return a welcome message at the root endpoint."""
    return {"message": "Welcome to GlobeTales API"}

@app.get("/health")
def health() -> dict[str, str]:
    """Return a simple health check response for the API."""
    return {"status": "ok"}
