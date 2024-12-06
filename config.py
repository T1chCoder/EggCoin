from dotenv import load_dotenv
import os 

load_dotenv()

# SECURITY WARNING: Keep the bot API token in production secret!
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

# Bot settings
MESSAGE_CLEAR = eval(os.getenv("MESSAGE_CLEAR", "False"), {"__builtins__": None}) == True