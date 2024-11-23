from dotenv import load_dotenv
import os 

load_dotenv()

# SECURITY WARNING: Keep the server key used in production secret!
SERVER_KEY = os.getenv("SERVER_KEY")

# SECURITY WARNING: Keep the API keys used in production secret!
API_V1_KEY = os.getenv("API_V1_KEY")

# SECURITY WARNING: Keep the bot API token in production secret!
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

# SECURITY WARNING: Keep the admin panel key in production secret!
ADMIN_PANEL_KEY = os.getenv("ADMIN_PANEL_KEY")

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = eval(os.getenv("DEBUG", "False")) == True

# List of allowed hosts for the server
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", [])

# Database credentials and settings
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_URL = f"mysql+aiomysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Path for template files
TEMPLATE_URL = "/templates/"

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

# Media files
MEDIA_URL = "/media/"

# Redirect URL after login
LOGIN_REDIRECT_URL = "home"

# Maximum number of fields allowed in uploaded data
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10485760

# Name of the web application
WEB_NAME = os.getenv("EggCoin", "")

# Bot settings
MESSAGE_CLEAR = eval(os.getenv("MESSAGE_CLEAR", "False"), {"__builtins__": None}) == True