# app/celery_app.py
from celery import Celery

celery_app = Celery(
    "app",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def add(x, y):
    return x + y