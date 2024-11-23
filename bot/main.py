import telebot
import config
import sys
from bot.buttons import reply
from bot.service import views as sv
from bot import commands, actions, utils, views,  handlers

bot = telebot.TeleBot(config.BOT_API_TOKEN)

def init():
    handlers.view_handle()
    bot.polling()