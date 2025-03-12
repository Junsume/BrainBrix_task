from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter()

# Route to create a new todo item
@router.post("/todos/", response_model=schemas.TodoItem)
def create_todo(todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = models.TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Route to get all todo items with pagination and sorting
@router.get("/todos/", response_model=list[schemas.TodoItem])
def read_todos(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Maximum number of items to return"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    order: str = Query("asc", description="Order of sorting: asc or desc"),
    db: Session = Depends(get_db)
):
    query = db.query(models.TodoItem).filter(models.TodoItem.is_deleted == False)

    # Sorting logic
    if sort_by == "created_at":
        query = query.order_by(models.TodoItem.created_at.asc() if order == "asc" else models.TodoItem.created_at.desc())
    elif sort_by == "updated_at":
        query = query.order_by(models.TodoItem.updated_at.asc() if order == "asc" else models.TodoItem.updated_at.desc())
    elif sort_by == "completed":
        query = query.order_by(models.TodoItem.completed.asc() if order == "asc" else models.TodoItem.completed.desc())

    todos = query.offset(skip).limit(limit).all()
    return todos

# Route to get a todo item by ID
@router.get("/todos/{todo_id}", response_model=schemas.TodoItem)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id, models.TodoItem.is_deleted == False).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Route to update a todo item
@router.put("/todos/{todo_id}", response_model=schemas.TodoItem)
def update_todo(todo_id: int, todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id, models.TodoItem.is_deleted == False).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Route to delete a todo item (soft delete)
@router.delete("/todos/{todo_id}", response_model=schemas.TodoItem)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.is_deleted = True  # Soft delete
    db.commit()
    return db_todo