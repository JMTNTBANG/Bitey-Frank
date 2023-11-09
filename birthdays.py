import discord
import os
from os import getenv
from dotenv import load_dotenv

import csv

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)

load_dotenv()
if 'debug' in os.listdir('./'):
    token = getenv('DEBUGTOKEN')
else:
    token = getenv('TOKEN')
if token is None:
    print('GIMMIE YO GODDAMN TOKEN B***CH')
    exit(1)

@client.event
async def on_ready():
