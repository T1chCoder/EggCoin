from app import app 
import views

app.add_url_rule("/", "home", views.HomeView())