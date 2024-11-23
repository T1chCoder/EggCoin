from web import app, views
import config

app = app.get

async def init():
  from web import views
  app.run(debug=config.DEBUG)