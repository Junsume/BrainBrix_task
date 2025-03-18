from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class TodoItem(BaseModel):
    id: str = None  # MongoDB ObjectId will be converted to string
    title: str
    description: str = None
    completed: bool = False
    created_at: datetime = None
    updated_at: datetime = None
    is_deleted: bool = False

    class Config:
        orm_mode = True