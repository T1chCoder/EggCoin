from bot.service import views as sv
from bot import views 

class HomeReplyButton(sv.ReplyButtonView):
  text = "🔙 Back"
  pages = [views.ProfileView, views.FriendsView, views.StatsView, views.HelpView, views.SupportView]
  redirect_to = views.HomeView
  
class ProfileReplyButton(sv.ReplyButtonView):
  text = "👤 Profile"
  pages = [views.HomeView]
  redirect_to = views.ProfileView
  
class FriendsReplyButton(sv.ReplyButtonView):
  text = "🤝 Friends"
  pages = [views.HomeView]
  redirect_to = views.FriendsView
  
class StatsReplyButton(sv.ReplyButtonView):
  text = "📊 Stats"
  pages = [views.HomeView]
  redirect_to = views.StatsView
  
class HelpReplyButton(sv.ReplyButtonView):
  text = "❓ Help"
  pages = [views.HomeView]
  redirect_to = views.HelpView
  
class SupportReplyButton(sv.ReplyButtonView):
  text = "🛠 Support"
  pages = [views.HomeView]
  redirect_to = views.SupportView