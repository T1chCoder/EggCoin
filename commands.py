from service import views as sv
import views 

class StartCommandView(sv.CommandView):
  text = "start"
  redirect_to = views.HomeView
  
class ProfileCommandView(sv.CommandView):
  text = "profile"
  redirect_to = views.ProfileView
  
class FriendCommandView(sv.CommandView):
  text = "friend"
  redirect_to = views.FriendsView
  
class StatsCommandView(sv.CommandView):
  text = "stats"
  redirect_to = views.StatsView
  
class HelpCommandView(sv.CommandView):
  text = "help"
  redirect_to = views.HelpView
  
class SupportCommandView(sv.CommandView):
  text = "support"
  redirect_to = views.SupportView