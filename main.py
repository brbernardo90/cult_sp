from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

import crud, schemas, models, database

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

# Endpoint to test database connectivity
@app.get("/test-db")
def test_database_connection():
    try:
        # Attempt to create a database session
        db = database.SessionLocal()
        db.execute(text("SELECT 1"))  # Run a simple query
        db.close()
        return {"message": "Database connection is successful!"}
    except OperationalError as e:
        return {"error": "Failed to connect to the database.", "details": str(e)}

# Initialize database models
models.Base.metadata.create_all(bind=database.engine)

@app.get("/events", response_model=list[schemas.Event])
def get_all_events(db: Session = Depends(database.get_db)):
    return crud.get_all_events(db)

@app.get("/events/upcoming", response_model=list[schemas.Event])
def get_upcoming_events(db: Session = Depends(database.get_db)):
    return crud.get_upcoming_events(db)


