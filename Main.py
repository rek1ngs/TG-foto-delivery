import logging
from os import getenv
import asyncio
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from handler import waterMark

load_dotenv(find_dotenv())

TOKEN = getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
rt = Router()

# @dp.message(F.text)
# async def echo(message: Message):
#     await bot.send_message(
#         chat_id = message.chat.id,
#         text= "wait"
#     )
#     await message.answer(text=message.text)

async def main():

    print("Let's go!")

    waterMark.register_handlers(dp)

    logging.basicConfig(level=logging.INFO)
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())