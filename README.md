# Todo App with FastAPI and PostgreSQL

## Project Overview

The Todo App is a backend application built using FastAPI that allows users to create, read, update, and delete todo items. This application integrates with a PostgreSQL database, providing a practical example of RESTful API design, database integration, and backend development practices.

## Features

- **CRUD Operations**: 
  - Create, read, update, and delete todo items.
  
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
│   ├── database.py            # setup for interacting with a database using SQLAlchemy in a Python application
│   ├── models.py              # SQLAlchemy models for todo items (Defining the table todo_items)
│   ├── schemas.py             # Pydantic models for data validation
│   └── routes.py              # API route definitions
│
├── create_tables.py           # (Optional) Creating the table defined in models.py, (run by -> `python create_tables.py`)
├── tasks.json                 # data file
├── test_main.py               
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
This will execute all the test functions in the test_main.py file and report the results.



## API Development

### Endpoints

- **Create Todo Item**: `POST /todos`
- **Read Todo Items**: `GET /todos`
- **Update Todo Item**: `PUT /todos/{id}`
- **Delete Todo Item**: `DELETE /todos/{id}`

### Input and Output Validation

- Input and output are validated using Pydantic models to ensure data integrity.

### API Documentation

- The API documentation is available at `http://127.0.0.1:8000/docs` after running the application.

## Testing

- Tests for the API endpoints can be written using FastAPI’s `TestClient` or `pytest`.
- Ensure that all tests pass before deploying the application.

## Running the Application

To run the application, use the following command:

```bash
uvicorn app.main:app --reload
```

Access the application at `http://127.0.0.1:8000`.
