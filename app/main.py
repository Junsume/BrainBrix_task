from fastapi import FastAPI
from app.celery_app import add, process, celery_app
from celery.result import AsyncResult

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Celery with Docker"}

@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    result = add.delay(a, b)  # call async task
    return {"task_id": result.id}

@app.get("/process/{a}/{b}")
def process_numbers(a: int, b: int):
    result = process.delay(a, b)
    return {"task_id": result.id}

# Fetch result by task ID
@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    if result.state == "PENDING":
        return {"status": "PENDING", "result": None}
    elif result.state == "FAILURE":
        return {"status": "FAILURE", "result": str(result.result)}
    else:
        return {"status": result.state, "result": result.result}