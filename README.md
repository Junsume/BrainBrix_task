# Todo App with FastAPI and PostgreSQL OR Mongo DB
This branch contains two implementations of a Todo application:

- **PostgreSQL Todo App**: A Todo application using PostgreSQL as the database.
- **MongoDB Todo App**: A Todo application using MongoDB as the database.

## Features

- Create, read, update, and delete todo items
- Sorting and pagination

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Junsume/BrainBrix_task.git
   cd BrainBrix_task
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Configure the database connection in the respective app directories.

## Running the Apps

### For MongoDB Todo App

Run the application with:
```bash
uvicorn MongoDB_todo.app.main:app --reload
```

### For PostgreSQL Todo App

Run the application with:
```bash
uvicorn PostgreSQL_todo.app.main:app --reload
```

Access the API documentation at `http://127.0.0.1:8000/docs`.
