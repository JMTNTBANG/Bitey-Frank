import discord
from dotenv import load_dotenv
from os import getenv

def start():
    load_dotenv()
    TOKEN = getenv('TOKEN')
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} active')

    client.run(TOKEN)