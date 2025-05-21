from fastapi import FastAPI
from app.celery_app import add

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Celery with Docker"}

@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    result = add.delay(a, b)  # call async task
    return {"task_id": result.id}
