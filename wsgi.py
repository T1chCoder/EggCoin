from fastapi.middleware.wsgi import WSGIMiddleware
from web import main as web
from api import main as api 

api.app.mount("/", WSGIMiddleware(web.app))

app = api.app

def init():
  import uvicorn
  uvicorn.run(api.app, host="127.0.0.1", port=8000)