from fastapi import FastAPI

from src.models import Healthy, Fibonacci, AddOne
from src.package_a.module_x import fib
from src.package_b.module_y import add_one

app = FastAPI()


@app.get("/")
async def root() -> Healthy:
    return Healthy()


@app.post("/fib")
async def fib_endpoint(payload: Fibonacci) -> int:
    return fib(payload.number)


@app.post("/add-one")
async def add_one_endpoint(payload: AddOne) -> int:
    return add_one(payload.number)
