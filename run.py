from app import bot
import handlers

def set_webhook():
    import config
    bot.remove_webhook()
    bot.set_webhook(url=config.WEBHOOK_URL)

def init():
    handlers.view_handle()

if __name__ == "__main__":
    set_webhook()
    init()