import logging 
from sqlmodel import Session

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler('logs/db.log', encoding="utf-8"), logging.StreamHandler()])

def log_info(message):
  logging.info(message)
  
def log_error(exception):
  logging.error(f"Error occurred: {exception}")
  
def get_db():
  from db.main import engine
  with Session(engine) as session:
        yield session