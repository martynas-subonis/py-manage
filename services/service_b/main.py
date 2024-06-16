from fastapi import FastAPI

from src.models import Healthy

app = FastAPI()


@app.get("/")
async def root() -> Healthy:
    return Healthy()
