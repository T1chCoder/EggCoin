import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler('logs/info.log', encoding="utf-8"), logging.StreamHandler()])

def info(message):
	logging.info(message)

def error(exception):
  logging.error(exception)