from app import bot
import handlers

def init():
    handlers.view_handle()
    bot.polling()

if __name__ == "__main__":
    init()