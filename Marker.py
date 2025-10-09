from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def watermark(image_bytes: BytesIO):
    watermark_image = Image.open(image_bytes).convert("RGBA")
    txt_layer = Image.new('RGBA', watermark_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    w, h = watermark_image.size
    font_size = int(h / 2)
    x, y = int(w / 2), int(h / 2)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Arial.ttf", 100)
    except OSError:
        font = ImageFont.load_default()

    draw.text((x, y), "Mellon", fill=(0, 0, 0,255), font=font, anchor='ms')

    watermarked = Image.alpha_composite(watermark_image, txt_layer)

    output_bytes = BytesIO()
    watermarked.convert("RGB").save(output_bytes, format='JPEG')
    output_bytes.seek(0)

    return output_bytes
