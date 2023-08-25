from PIL import Image, ImageDraw, ImageFont


def generate_image(text:str, name:str):
    image = Image.new("RGB", (1920, 1080), (0, 0, 0))
    textt = ImageDraw.Draw(image)
    font = ImageFont.truetype("./fixedsys.ttf", 250)
    _, _, w, h = textt.textbbox((0, 0), text, font=font)
    textt.text(((1920-w)/2, (1080-h)/2), text, font=font)
    image.save(f"./{name}")

def generate_gif(text:str, text2:str, dur:int, name:str):
    images = []
    image1 = Image.new("RGB", (1920, 1080), (0, 0, 0))
    textt1 = ImageDraw.Draw(image1)
    font = ImageFont.truetype("./fixedsys.ttf", 250)
    _, _, w, h = textt1.textbbox((0, 0), text, font=font)
    textt1.text(((1920 - w) / 2, (1080 - h) / 2), text, font=font)
    images.append(image1)
    image2 = Image.new("RGB", (1920, 1080), (0, 0, 0))
    textt2 = ImageDraw.Draw(image2)
    font = ImageFont.truetype("./fixedsys.ttf", 250)
    _, _, w, h = textt2.textbbox((0, 0), text2, font=font)
    textt2.text(((1920 - w) / 2, (1080 - h) / 2), text2, font=font)
    images.append(image2)
    images[0].save(f"./{name}",
                   save_all=True, append_images=images[1:], optimize=False, duration=dur, loop=0)
