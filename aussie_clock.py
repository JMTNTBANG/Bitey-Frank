import discord
import os
import asyncio
from pytz import timezone
from datetime import datetime
from image_tools import generate_gif
from dotenv import load_dotenv
from os import getenv

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)

roles: dict[str, discord.Role] = {}
aus_time = ""

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
                generate_gif(aussie_time.strftime('%H:%M'), aussie_time.strftime('%H %M'), 1000, "aussie_clock.gif")
                with open('aussie_clock.gif', 'rb') as f:
                    picture = f.read()
                await guild.edit(banner=picture)
                aus_time = aussie_time.strftime('%H:%M')

            
            
@client.event
async def on_ready():
    for guild in client.guilds:
        for role in guild.roles:
            roles[f'@{role.name}'] = role

    while True:
        await aussie_tz()
        
client.run(token)
