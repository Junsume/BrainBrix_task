import asyncio
import json
from app.database import database
from app.models import TodoItem
from datetime import datetime

async def populate_db():
    # Load data from JSON file
    with open('tasks.json', 'r') as file:
        todos_data = json.load(file)

    # Prepare the data for insertion
    todos = []
    for todo_data in todos_data:
        todo = TodoItem(
            title=todo_data["title"],
            description=todo_data.get("description", ""),
            completed=todo_data.get("completed", False),  # Map 'completed' to 'done'
            created_at=datetime.fromisoformat(todo_data["created_at"]),
            updated_at=datetime.fromisoformat(todo_data["updated_at"]),
            is_deleted=todo_data.get("is_deleted", False)  # Include is_deleted field
        )
        todos.append(todo.model_dump(exclude={"id"}))  # Exclude 'id' as it will be generated by MongoDB

    # Insert all todos into the database
    await database["todos"].insert_many(todos)
    print("Database populated with todo items from JSON file.")

if __name__ == "__main__":
    asyncio.run(populate_db())