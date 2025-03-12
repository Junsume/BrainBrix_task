from pydantic import BaseModel
from datetime import datetime

class TodoItemBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TodoItemCreate(TodoItemBase):
    pass

class TodoItem(TodoItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        orm_mode = True