from app import app 
import views

app.add_url_rule("/", "home", views.HomeView())
app.add_url_rule("/webhook", "webhook", views.WebHookView())