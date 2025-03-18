from fastapi import APIRouter, HTTPException, Query
from app.database import database
from app.schemas import TodoItem, TodoItemCreate, TodoItemUpdate
from bson import ObjectId
from datetime import datetime

router = APIRouter()

# Route to create a new todo item
@router.post("/todos/", response_model=TodoItem)
async def create_todo(todo: TodoItemCreate):
    # Validate input
    if not todo.title:
        raise HTTPException(status_code=400, detail="Title is required")

    # Create a new todo item
    todo_item = TodoItem(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_deleted=False
    )

    # Insert the todo item into the database
    result = await database["todos"].insert_one(todo_item.dict())
    todo_item.id = str(result.inserted_id)  # Set the ID to the inserted document's ID
    return todo_item

# Route to get all todo items with pagination and sorting
@router.get("/todos/", response_model=list[TodoItem])
async def read_todos(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Maximum number of items to return"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    order: str = Query("asc", description="Order of sorting: asc or desc")
):
    valid_sort_fields = ["created_at", "updated_at", "completed"]
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail="Invalid sort_by parameter")

    query = {"is_deleted": False}  # Filter out soft-deleted items
    todos = []
    async for todo in database["todos"].find(query).sort(sort_by, 1 if order == "asc" else -1).skip(skip).limit(limit):
        todo["id"] = str(todo["_id"])  # Convert ObjectId to string
        todos.append(todo)
    return todos

# Route to get a todo item by ID
@router.get("/todos/{todo_id}", response_model=TodoItem)
async def read_todo(todo_id: str):
    todo = await database["todos"].find_one({"_id": ObjectId(todo_id), "is_deleted": False})
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo["id"] = str(todo["_id"])  # Convert ObjectId to string
    return todo

# Route to update a todo item
@router.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: str, todo: TodoItemUpdate):
    update_data = todo.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()  # Update the timestamp

    result = await database["todos"].update_one({"_id": ObjectId(todo_id), "is_deleted": False}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_todo = await read_todo(todo_id)  # Fetch the updated todo item
    return updated_todo

# Route to delete a todo item (soft delete)
@router.delete("/todos/{todo_id}", response_model=TodoItem)
async def delete_todo(todo_id: str):
    result = await database["todos"].update_one({"_id": ObjectId(todo_id)}, {"$set": {"is_deleted": True}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": todo_id, "is_deleted": True}

# Route to hard delete a todo item
@router.delete("/todos/hard/{todo_id}", response_model=TodoItem)
async def hard_delete_todo(todo_id: str):
    result = await database["todos"].delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": todo_id, "deleted": True}