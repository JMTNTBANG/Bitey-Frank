import discord
import os
import asyncio
from pytz import timezone
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import getenv
from PIL import Image, ImageDraw, ImageFont

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)

roles: dict[str, discord.Role] = {}
aus_time = ""
schedule = {
    "mon": 0,
    "tue": 0,
    "wed": 0,
    "thu": 0,
    "fri": 0
}

load_dotenv()
if 'debug' in os.listdir('./'):
    token = getenv('DEBUGTOKEN')
else:
    token = getenv('TOKEN')
if token is None:
    print('GIMMIE YO GODDAMN TOKEN B***CH')
    exit(1)


async def aussie_tz():
    aussie_timezone = timezone("Australia/Adelaide")
    aussie_time = datetime.now(aussie_timezone)
    global aus_time
    if aussie_time.strftime('%H:%M') != aus_time:
        for guild in client.guilds:
            if guild.name == "Garbage Stream":
                text_list = [
                    aussie_time.strftime('%H:%M'),
                    aussie_time.strftime('%H %M')
                ]
                images = []
                for text in text_list:
                    image = Image.new("RGB", (1920, 1080), (0, 0, 0))
                    draw = ImageDraw.Draw(image)
                    font = ImageFont.truetype("./fixedsys.ttf", 250)
                    _, _, w, h = draw.textbbox((0, 0), text, font=font)
                    draw.text(((1920 - w) / 2, (1080 - h) / 2), text, font=font)
                    images.append(image.copy())
                    if ( text.startswith("09") and aussie_time.weekday() in (1, 2, 4) or # 9 AM Tue, Wed, Fri
                         text.startswith("17") and aussie_time.weekday() in (0, 3) ):    # 5 PM Mon, Thu
                        font = ImageFont.truetype("./fixedsys.ttf", 125)
                        _, _, w, h = draw.textbbox((0, 0), "It's Goobin Time!", font=font)
                        draw.text(((1920 - w) / 2, (1400 - h) / 2), "It's Goobin Time!", font=font, fill="#00ff00")
                        images.append(image)
                        images[-1], images[-2] = images[-2], images[-1] # switch goobin' and non-goobin' message so goobin' is first frame
                images[0].save(f"./aussie_clock.gif", save_all=True, append_images=images[1:], optimize=False, duration=1000/len(images), loop=0)
                with open('aussie_clock.gif', 'rb') as f:
                    picture = f.read()
                await guild.edit(banner=picture)
                aus_time = aussie_time.strftime('%H:%M')

                # if "09:" in aussie_time.strftime('%H:%M'):
                # font = ImageFont.truetype("./fixedsys.ttf", 125)
                # goobtime = ImageDraw.Draw(image1)
                # _, _, w, h = goobtime.textbbox((0, 0), "It's Goobin Time!", font=font)
                # goobtime.text(((1920 - w) / 2, (1620 - h) / 2), "It's Goobin Time!", font=font)
                # images.append(image1)


def goob_schedule_upd():
    aussie_timezone = timezone("Australia/Adelaide")
    aussie_date = datetime.now(aussie_timezone)
    global schedule
    this_week = {}
    for day in range(5):
        hour = 0
        if day in (1, 2, 4):
            hour = 9
        elif day in (0, 3):
            hour = 17
        this_week[day] = aussie_date + timedelta(days=-aussie_date.weekday() + day,
                                                 weeks=1,
                                                 hours=-aussie_date.hour + hour,
                                                 minutes=-aussie_date.minute,
                                                 seconds=-aussie_date.second,
                                                 microseconds=-aussie_date.microsecond)


@client.event
async def on_ready():
    for guild in client.guilds:
        for role in guild.roles:
            roles[f'@{role.name}'] = role

    while True:
        await aussie_tz()
        await asyncio.sleep(60 - datetime.now().second)

client.run(token)
