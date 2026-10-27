
from fastapi import FastAPI
from app.api.routes.tasks import router as tasks_router
app = FastAPI(title="Task Knowledge API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
app.include_router(tasks_router)