from flask import render_template as render
from web import app 

app = app.get

@app.route("/")
def home():
	return render(f"/leads/home.html")