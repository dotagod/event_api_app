from fastapi import FastAPI

from app.api.events import router as events_router

app = FastAPI()
app.include_router(events_router)
