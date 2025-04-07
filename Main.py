from dotenv import load_dotenv, find_dotenv
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, F
import logging
from aiogram.types import Message

load_dotenv(find_dotenv())

TOKEN = getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()
rt = Router()

@dp.message(F.text)
async def echo(message: Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text= "wait"
    )
    await message.answer(text=message.text)

@rt.message(F.photo)
async def photo_handler(message: Message):
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path

    # Save to disk
    save_path = f"photos/userid_{message.from_user.id}.jpg"
    await bot.download_file(file_path, destination=save_path)

    print("save")

    await message.reply("Photo received and saved!")

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())