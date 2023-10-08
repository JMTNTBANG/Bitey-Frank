import discord
import os
from youtube_tools import get_latest_video
from dotenv import load_dotenv
from os import getenv
import asyncio
import datetime

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)

roles: dict[str, discord.Role] = {}

channels: list = [
    "Dankmus",
    "DankPods",
    "GarbageTime420",
    "the.drum.thing.",
    "HelloImGaming",
    "Games_for_James",
    "JMTNTBANG",
    "joshdoesntplaydrums"
]

load_dotenv()
if 'debug' in os.listdir('./'):
    token = getenv('DEBUGTOKEN')
else:
    token = getenv('TOKEN')
if token is None:
    print('GIMMIE YO GODDAMN TOKEN B***CH')
    exit(1)


def calc_wait_time(interval: float):
    now = datetime.datetime.now()
    return interval - ((now.minute * 60 + now.second) % interval)

        

async def yt_checker(ytchannel):
    latest_video = get_latest_video(f'@{ytchannel}')
    if f'{ytchannel}.txt' not in os.listdir('./youtube'):
        open(f'youtube/{ytchannel}.txt', 'x')
    if f'N: {latest_video.title} U: {latest_video.url} T: {latest_video.published}' != open(f'youtube/{ytchannel}.txt', 'r').readline():
        open(f'youtube/{ytchannel}.txt', 'w').write(f'N: {latest_video.title} U: {latest_video.url} T: {latest_video.published}')
        response = f'{roles[f"@{latest_video.channel} Ping"].mention} New video by {latest_video.channel}! `{latest_video.title}`\n' \
            f'Uploaded <t:{int(latest_video.published.timestamp())}:R>\n' \
            f'{latest_video.url}'
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.topic is not None:
                    if 'YouTube Ping' in channel.topic:
                        await channel.send(response)
                        print(f"Sent {ytchannel} ping!")


@client.event
async def on_ready():
    for guild in client.guilds:
        for role in guild.roles:
            roles[f'@{role.name}'] = role

    while True:
        from googleapiclient.errors import HttpError
        try:
            for channel in channels:
                await (yt_checker(channel))
        except HttpError:
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if 'YouTube Ping' in channel.topic:
                            await channel.send("<@348935840501858306> Help, google api is being a dingus again :/")
                        print(f"Google API Error")
            raise
        else:

            await asyncio.sleep(calc_wait_time(300))
        
client.run(token)
