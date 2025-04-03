from dotenv import load_dotenv, find_dotenv
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, types
import logging

# from aiogram import Bot, Dispatcher, html
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.types import Message
load_dotenv(find_dotenv())

TOKEN = getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text= "wait"
    )
    await message.answer(text=message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())