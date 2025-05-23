# app/celery_app.py
from celery import Celery
from time import sleep

celery_app = Celery(
    "app",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def process(x, y):
    i = 0
    while i < 35:
        sleep(1)
        i += 1
        print("processing...")
    return x**2 + y**3