import telebot
from telebot import types
from data import get as data
from data import change as data_change
import actions

reply_keyboard_markup = []

class TemplateView:
  text = None 
  markup = None 
  
  def __init__(self, bot, message):
    self.bot = bot
    self.message = message
    self.markup_handle()
   
  def message_handle(self):
    if self.text:
      actions.message_clear(self.message)
      message = self.bot.send_message(self.message.chat.id, self.text, parse_mode="Markdown", reply_markup=self.markup)
      data_change.page(self.__class__)
      actions.message_add(self.message)
      actions.message_add(message)
      actions.log_message(self.message, message)
    else:
      actions.log_error("No text provided")
    
  def markup_handle(self):
    from handlers import reply_buttons
    
    markup = types.ReplyKeyboardRemove()
    if not self.markup and reply_buttons():
      reply_button_texts = []
      for reply_button in reply_buttons():
        if self.__class__ in reply_button.pages:
          reply_button_texts.append(reply_button.text)
      if reply_button_texts:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        for reply_button_text in reply_button_texts:
          markup.add(types.KeyboardButton(text=reply_button_text))
    self.markup = markup
    
  def handle(self):
    self.message_handle()
    
class CommandView:
  redirect_to = None
  
  def __init__(self, bot, message):
    self.bot = bot  
    self.message = message
    
  def handle(self):
    if self.redirect_to:
      actions.log_command(self.message)
      self.redirect_to(bot=self.bot, message=self.message).handle()
    else:
      actions.log_error("Redirect page not provided")
      
class ReplyButtonView:
  text = None 
  pages = []
  redirect_to = None 
  
  def __init__(self, bot, message):
    self.bot = bot  
    self.message = message 
    
  def handle(self):
    if self.text:
      if self.redirect_to:
        actions.log_button(self.message)
        self.redirect_to(bot=self.bot, message=self.message).handle()
      else:
        actions.log_error("Redirect page not provided")
    else:
      actions.log_error("No text provided")