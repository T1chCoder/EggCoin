from app import bot
import handlers

def set_webhook():
    import config
    webhook_url = config.WEBHOOK_URL
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

def init():
    handlers.view_handle()
    bot.polling()

if __name__ == "__main__":
    set_webhook()
    init()