from flask import render_template as render, request

class HomeView:
  def __call__(self):
    return render("leads/home.html")
  
class WebHook:
  def __call__(self):
    if request.headers.get('content-type') == 'application/json':
        return '', 200
    return '', 403