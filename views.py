from flask import render_template as render

class HomeView:
  def __call__(self):
    return render("leads/home.html")