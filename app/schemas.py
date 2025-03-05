from pydantic import BaseModel

class TodoItemBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TodoItemCreate(TodoItemBase):
    pass

class TodoItem(TodoItemBase):
    id: int

    class Config:
        orm_mode = True