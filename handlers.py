from service import views as sv
from data import get as data

def reply_buttons():
  reply_button_view_subclasses = sv.ReplyButtonView.__subclasses__()
  if reply_button_view_subclasses:
    reply_button_views = reply_button_view_subclasses[:]
    
    for reply_button_view_subclass in reply_button_view_subclasses:
      reply_button_views.extend(reply_button_view_subclass.__subclasses__())
    
    return reply_button_views
  return []

def commands():
  command_view_subclasses = sv.CommandView.__subclasses__()
  
  if command_view_subclasses:
    command_views = command_view_subclasses[:]
    
    for command_view_subclass in command_view_subclasses:
      command_views.extend(command_view_subclass.__subclasses__())
      
    return command_views
  return []

def view_handle():
  from app import bot 
  
  command_views = commands()
  reply_button_views = reply_buttons()
  
  if command_views:
    @bot.message_handler(func=lambda message: message.text.startswith("/"))
    def command_handle(message):
      
      for command_view in command_views:
        if message.text == f"/{command_view.text}":
          command_view = command_view(bot, message)
          command_view.handle()
          break
    
  if reply_button_views:
    reply_button_texts = []
    
    for reply_button_view in reply_button_views:
      reply_button_texts.append(reply_button_view.text)
    
    @bot.message_handler(func=lambda message: not message.text.startswith("/") and message.text in reply_button_texts)
    def reply_button_handle(message):
      for reply_button_view in reply_button_views:
        if data.page() in reply_button_view.pages:
          reply_button_view = reply_button_view(bot, message)
          reply_button_view.handle()
          break