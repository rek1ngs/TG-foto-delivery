import logging
from os import getenv
import asyncio
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from handler import waterMark
from prometheus_client import start_http_server, Counter
import time


load_dotenv(find_dotenv())

TOKEN = getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
rt = Router()

start_http_server(8000)
REQUEST_COUNTER = Counter('telegram_bot_requests_total', 'Total number of requests received by the Telegram bot')

async def metrics():
    while True:
        REQUEST_COUNTER.inc()
        await asyncio.sleep(5)

async def main():

    print("Let's go!")

    waterMark.register_handlers(dp)

    logging.basicConfig(level=logging.INFO)
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())