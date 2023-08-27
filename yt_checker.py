import discord
import os
from youtube_tools import get_latest_video
from dotenv import load_dotenv
from os import getenv

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)

roles: dict[str, discord.Role] = {}

load_dotenv()
if 'debug' in os.listdir('./'):
    token = getenv('DEBUGTOKEN')
else:
    token = getenv('TOKEN')
if token is None:
    print('GIMMIE YO GODDAMN TOKEN B***CH')
    exit(1)

        
async def yt_check():
    async def checker(ytchannel):
        a = get_latest_video(f'@{ytchannel}')
        if f'{ytchannel}.txt' not in os.listdir('./youtube'):
            open(f'youtube/{ytchannel}.txt', 'x')
        if f'N: {a.title} U: {a.url} T: {a.published}' != open(f'youtube/{ytchannel}.txt', 'r').readline():
            open(f'youtube/{ytchannel}.txt', 'w').write(f'N: {a.title} U: {a.url} T: {a.published}')
            response = f'{roles[f"@{a.channel} Ping"].mention} New video by {a.channel}! `{a.title}`\n' \
                f'Uploaded <t:{int(a.published.timestamp())}:R>\n' \
                f'{a.url}'
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if 'YouTube Ping' in channel.topic:
                            await channel.send(response)
                            print(f"Sent {ytchannel} ping!")

    await checker('Dankmus')
    await checker('DankPods')
    await checker('GarbageTime420')
    await checker('the.drum.thing.')
    await checker('HelloImGaming')
    await checker('Games_for_James')
    await checker('JMTNTBANG')
    await checker('joshdoesntplaydrums')
            
            
@client.event
async def on_ready():
    for guild in client.guilds:
        for role in guild.roles:
            roles[f'@{role.name}'] = role

    while True:
        await yt_check()
        
client.run(token)
