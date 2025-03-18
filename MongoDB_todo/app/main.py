from fastapi import FastAPI
from app.routes import router  # Import your router from routes.py
from app.database import database  # Import your database connection

app = FastAPI()

# Include the router for the todo routes
app.include_router(router, prefix="/api", tags=["todos"])

@app.on_event("startup")
async def startup_db():
    # Any startup tasks can be done here, like connecting to the database
    pass

@app.on_event("shutdown")
async def shutdown_db():
    # Any cleanup tasks can be done here, like closing the database connection
    await database.client.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Todo API!"}

# You can add more routes or middleware here if needed