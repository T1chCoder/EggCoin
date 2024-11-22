import telebot
from telebot import types
import config
import sys
from bot.buttons import reply
from bot.service import views as sv
from bot import commands, actions, utils, views,  handlers

bot = telebot.TeleBot(config.BOT_API_TOKEN)

def start():
    try:
        handlers.view_handle()
        actions.log_info("Bot started successfully and is now running")
        bot.polling()
    except KeyboardInterrupt:
        stop()
    except Exception as e:
        stop()
        actions.log_error(e)
    finally:
        stop()

def stop():
    actions.log_info("Bot has been gracefully stopped and shut down")
    bot.stop_polling()
    sys.exit()

if __name__ == '__main__':
    start()