from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="Syncrova CodeMentor API",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(analyze_router)


@app.get("/")
def root():
    return {
        "message": "Syncrova CodeMentor API is running!"
    }