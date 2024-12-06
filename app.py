import telebot
import config
from buttons import reply
from service import views as sv
import commands, actions, utils, views, handlers

bot = telebot.TeleBot(config.BOT_API_TOKEN)