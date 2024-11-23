import asyncio
import log
from bot import main as bot
from db import main as db
import uvicorn
import wsgi
import threading

async def main():
    try:
        await db.init()
        log.info("Database initialized successfully.")
        
        threading.Thread(target=bot.init).start()

        asyncio.create_task(wsgi_init())
        await asyncio.Event().wait()

    except Exception as e:
        log.error(e)
        raise

async def wsgi_init():
    try:
        uvicorn_config = uvicorn.Config(wsgi.app, host="127.0.0.1", port=8000)
        server = uvicorn.Server(uvicorn_config)
        await server.serve()
    except Exception as e:
        log.error(e)

if __name__ == "__main__":
    try:
        if not asyncio.get_event_loop().is_running():
            asyncio.run(main())
        else:
            log.error("Event loop is already running, cannot use asyncio.run() here.")
    except Exception as e:
        log.error(e)