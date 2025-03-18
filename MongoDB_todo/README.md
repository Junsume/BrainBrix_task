# Todo App

A simple Todo application built with FastAPI and MongoDB.

## Features

- Create, read, update, and soft delete todo items
- Sorting and pagination

## Technologies

- **FastAPI**
- **MongoDB**

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

## Running the App

Run the application with:

```bash
uvicorn app.main:app --reload
```

Access the API at `http://127.0.0.1:8000/docs`.
