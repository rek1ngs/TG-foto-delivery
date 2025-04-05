from dotenv import load_dotenv, find_dotenv
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, types, Router, F
import logging
from aiogram.types import ContentType

load_dotenv(find_dotenv())

TOKEN = getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()
rt = Router()

@dp.message(F.text)
async def echo(message: types.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text= "wait"
    )
    await message.answer(text=message.text)

@rt.message(F.photo)
async def photo(message: types.Message):
    await message.answer(text = "This is foto")

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())