from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId

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
    id: str  # MongoDB ObjectId will be converted to string
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: str  # Convert ObjectId to string for JSON serialization
        }
