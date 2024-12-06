import config
import telebot
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler('info.log', encoding="utf-8"), logging.StreamHandler()])

def message_add(message):
  from data import main as data
  
  if config.MESSAGE_CLEAR:
    data.messages.append({"id": message.message_id, "chat_id": message.chat.id, "sender": {"id": message.from_user.id}})

def message_clear(message):
  from data import main as data
  from app import bot
  
  if config.MESSAGE_CLEAR and data.messages:
    messages_to_remove = []
    
    for saved_message in data.messages:
      if saved_message["chat_id"] == message.chat.id:
        try:
          bot.delete_message(chat_id=saved_message["chat_id"], message_id=saved_message["id"])
          messages_to_remove.append(saved_message)
        except telebot.apihelper.ApiTelegramException:
          log_error(f"Message {saved_message['id']} not found")
        except Exception as e:
          log_error(e)
          break

    for message_to_remove in messages_to_remove:
      data.messages.remove(message_to_remove)

def log_info(message):
  logging.info(message)
  
def log_message(message, sent_message):
  logging.info(f"Bot replied with: message {sent_message.message_id} to User: {message.from_user.id}")

def log_command(message):  
  logging.info(f"Command received: {message.text} from User: {message.from_user.id}")

def log_button(message):
  logging.info(f"Button pressed: {message.text} from User: {message.from_user.id}")

def log_error(exception):
  logging.error(f"Error occurred: {exception}")