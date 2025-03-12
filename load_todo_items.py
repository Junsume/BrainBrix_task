import json
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import TodoItem
from datetime import datetime

def load_todo_items_from_json(file_path):
    with open(file_path, 'r') as file:
        todo_items = json.load(file)

    db: Session = SessionLocal()
    try:
        for item in todo_items:
            todo_item = TodoItem(
                title=item['title'],
                description=item['description'],
                completed=item['completed'],
                created_at=datetime.fromisoformat(item['created_at']),
                updated_at=datetime.fromisoformat(item['updated_at']),
                is_deleted=item['is_deleted']
            )
            db.add(todo_item)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    load_todo_items_from_json('tasks.json')