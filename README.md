# Todo App with FastAPI and PostgreSQL

## Project Overview

The Todo App is a backend application built using FastAPI that allows users to create, read, update, and delete todo items. This application integrates with a PostgreSQL database, providing a practical example of RESTful API design, database integration, and backend development practices.

## Features

- **CRUD Operations**:
  - Create, read, update, and delete todo items.
- **Sorting**:
  - Sort todo items by completion status (`completed`), creation time (`created_at`), and update time (`updated_at`).
- **Pagination**:
  - Implement pagination for the read API to manage large datasets effectively.
- **Soft Delete**:
  - Implement soft delete functionality to mark todo items as deleted without removing them from the database.
- **Database Integration**:
  - Utilizes PostgreSQL for persistent storage of todo items.
- **API Documentation**:
  - Automatically generated API documentation using Swagger UI.

## Environment Setup

### Prerequisites

- Python (3.9+)
- PostgreSQL

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Junsume/BrainBrix_task.git
   cd BrainBrix_task/todo_app
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:

   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2
   ```

4. **Set Up PostgreSQL Database**:

   - Create a PostgreSQL database for the application.
   - Update the database connection settings in your application configuration.

## Project Structure

```
 todo_app/
 │
 ├── app/
 │   ├── __init__.py
 │   ├── main.py                # Entry point for the FastAPI application
 │   ├── database.py            # Setup for interacting with a database using SQLAlchemy
 │   ├── models.py              # SQLAlchemy models for todo items (Defining the table todo_items)
 │   ├── schemas.py             # Pydantic models for data validation
 │   └──routes.py               # API route definitions
 │
 │
 ├── create_tables.py           # (Optional) Creating the table defined in models.py (run by -> `python create_tables.py`)
 ├── tasks.json                 # Data file (if applicable)
 ├── test_main.py               # Tests for the application
 ├── load_todo_items.py         # Script to populate the database with sample todo items
 └── README.md                  # Project documentation
```

## Running the Tests

To run the tests, you can use pytest. Make sure you have pytest installed in your virtual environment:

```bash
pip install pytest
```

Then, you can run the tests from the command line:

```bash
pytest test_main.py
```

This will execute all the test functions in the `test_main.py` file and report the results.

## API Development

### Endpoints

- **Create Todo Item**: `POST /todos`
- **Read Todo Items**: `GET /todos`
  - Supports sorting by `created_at`, `updated_at`, and `completed`.
  - Supports pagination with `skip` and `limit` parameters.
- **Update Todo Item**: `PUT /todos/{id}`
- **Delete Todo Item (Soft Delete)**: `DELETE /todos/{id}`
- **Delete Todo Item (Hard Delete)**: `DELETE /todos/hard/{id}`

### Input and Output Validation

Input and output are validated using Pydantic models to ensure data integrity.

### API Documentation

The API documentation is available at `http://127.0.0.1:8000/docs` after running the application.

### Testing

Tests for the API endpoints can be written using FastAPI’s `TestClient` or `pytest`.
Ensure that all tests pass before deploying the application.

## Running the Application

To run the application, use the following command:

```bash
uvicorn app.main:app --reload
```

Access the application at `http://127.0.0.1:8000`.

## Populating the Database with Sample Data

To populate the database with 100 sample todo items, you can run the `load_todo_items.py` script. This script will create 100 entries in the `todo_items` table with alternating completion statuses.

### Running the Load Script

Ensure your database is set up and the application is configured correctly.

Run the script:

```bash
python load_todo_items.py
```

This will populate your database with sample data, allowing you to test the application effectively.

## Conclusion

This `README.md` provides a comprehensive overview of your Todo app, including features, setup instructions, database population, and testing. If you have any further questions or need additional modifications, feel free to ask!
