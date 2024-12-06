from fastapi import FastAPI
import actions, handlers
from app import app

def init():
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
  init()