from database import SessionLocal
from utils import load_data_from_json

db = SessionLocal()
load_data_from_json("data.json", db)
db.close()
