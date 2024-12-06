from dotenv import load_dotenv
import os 

load_dotenv()

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = eval(os.getenv("DEBUG", "False")) == True