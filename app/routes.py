from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
from . import models, schemas
from .database import get_db

router = APIRouter()

# Function to load tasks from a JSON file
def load_tasks_from_json(file_path: str):
    with open(file_path, 'r') as file:
        tasks = json.load(file)
    return tasks

# Route to create a new todo item
@router.post("/todos/", response_model=schemas.TodoItem)
def create_todo(todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = models.TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Route to get all todo items
@router.get("/todos/", response_model=list[schemas.TodoItem])
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.TodoItem).all()

# Route to get a todo item by ID
@router.get("/todos/{todo_id}", response_model=schemas.TodoItem)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Route to update a todo item
@router.put("/todos/{todo_id}", response_model=schemas.TodoItem)
def update_todo(todo_id: int, todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Route to delete a todo item
@router.delete("/todos/{todo_id}", response_model=schemas.TodoItem)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return db_todo

# Route to load tasks from a JSON file
@router.post("/load_tasks/")
def load_tasks(file_path: str = "tasks.json", db: Session = Depends(get_db)):
    tasks = load_tasks_from_json(file_path)
    for task in tasks:
        db_task = models.TodoItem(**task)
        db.add(db_task)
    db.commit()
    return {"message": "Tasks loaded successfully"}