from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Automatically set to current time
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # Automatically updated to current time on update
    is_deleted = Column(Boolean, default=False)  # Soft delete flag