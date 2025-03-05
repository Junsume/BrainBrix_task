from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router

# Create the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the router
app.include_router(router)

# Optional: Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API!"}