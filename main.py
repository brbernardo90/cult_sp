from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize FastAPI app
app = FastAPI()

# Load environment variables
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")

# Create the PostgreSQL database connection string
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

# Initialize database connection
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

@app.get("/")
def read_root():
    return {"message": "FastAPI with PostgreSQL is up and running!"}

@app.get("/test-db")
def test_database():
    """Test the database connection with a simple query."""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 'Database Connected!' AS message"))
            for row in result:
                return {"message": row["message"]}
    except SQLAlchemyError as e:
        return {"error": str(e)}
