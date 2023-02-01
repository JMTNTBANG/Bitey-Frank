import discord
from dotenv import load_dotenv
from os import getenv
from random import choice as randItem

def start():
    # Load Token
    load_dotenv()
    TOKEN = getenv('TOKEN')

    # Set Bot Intents
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    
    # Set Client Variable
    global client
    client = discord.Client(intents=intents)

    # Set Dynamic Variables
    global channels
    global emojis
    channels = []
    emojis = {}

    # Set Static Variables
    global frankMojis
    frankMojis = [
        ':chonkfronk',
        ':frank3:',
        ':sneakyfrank:',
        ':hideyhole:',
        ':jpeg:'
    ]

    # Set Functions/Lambdas
    printEmoji = lambda emoji: f'<:{emojis[emoji].name}:{emojis[emoji].id}>'
    async def memberStatusUpdate(inServer: bool, member):
        for channel in channels:
            if channel.guild == member.guild and member.guild.system_channel == channel:
                if inServer:
                    await channel.send(printEmoji(randItem(frankMojis)))
                else:
                    await channel.send(f'{printEmoji(":frank:")}7 {member.mention}')
                break

    # Set Events
    @client.event
    async def on_ready():
        print(f'{client.user} active')

        # Channel Detection
        for channel in client.get_all_channels():
            channels.append(channel)

        # Emoji Detection
        for guild in client.guilds:
            for emoji in guild.emojis:
                emojis[f':{emoji.name}:'] = emoji

    @client.event
    async def on_member_join(member):
        await memberStatusUpdate(True, member)

    @client.event
    async def on_member_remove(member):
        await memberStatusUpdate(False, member)
        
    # Finalize Bot
    client.run(TOKEN)