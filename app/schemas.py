from pydantic import BaseModel
from datetime import datetime

class TodoItemBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TodoItemCreate(TodoItemBase):
    pass

class TodoItemUpdate(BaseModel):
    title: str = None  # Optional, can be updated
    description: str = None  # Optional, can be updated
    completed: bool = None  # Optional, can be updated

class TodoItem(TodoItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        orm_mode = True