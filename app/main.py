from fastapi import FastAPI

from app.routes.health import router as health_router

app = FastAPI(
    title="Syncrova AI API",
    description="Universal AI Code Analysis Service",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Syncrova AI API"
    }