from fastapi import FastAPI
from api import actions, handlers, app

app = app.get

def start():
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)