from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"
    assert "id" in response.json()  # Ensure the ID is returned

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_todo():
    # First, create a todo item to update
    response = client.post("/todos/", json={"title": "Update Todo", "description": "Update Description"})
    todo_id = response.json()["id"]

    # Now, update the created todo item
    response = client.put(f"/todos/{todo_id}", json={"title": "Updated Todo", "description": "Updated Description", "completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] is True
    assert response.json()["title"] == "Updated Todo"

def test_delete_todo():
    # First, create a todo item to delete
    response = client.post("/todos/", json={"title": "Delete Todo", "description": "Delete Description"})
    todo_id = response.json()["id"]

    # Now, delete the created todo item
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id  # Ensure the correct todo item is returned

    # Verify that the todo item has been deleted
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404  # Should return 404 after deletion