from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

DATABASE_URL = "mongodb://localhost:27017"  # Update with your MongoDB connection string

client = AsyncIOMotorClient(DATABASE_URL)
database = client.todo_db  # Create or connect to a database named 'todo_db'