from io import BytesIO
from aiogram import types, Dispatcher, F
from aiogram.types import BufferedInputFile
from Marker import watermark

async def handle_photo(message: types.Message,bot):
    # 1️⃣ Get the biggest photo version
    photo = message.photo[-1]

    # 2️⃣ Download to bytes
    photo_bytes = BytesIO()
    await bot.download(photo.file_id, destination=photo_bytes)
    photo_bytes.seek(0)

    # 3️⃣ Open image with Pillow
    image = watermark(photo_bytes)

    # 6️⃣ Send the modified image back
    await message.answer_photo(photo=BufferedInputFile(image.getvalue(),filename="result.jpg"), caption="🖼 Here's your modified photo!")

def register_handlers(dp: Dispatcher):
    dp.message.register(handle_photo, F.photo)