import discord
from dotenv import load_dotenv
from os import getenv
import asyncio
import datetime
import json
import scrapetube
import googleapiclient.discovery
import parse

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)

roles: dict[str, discord.Role] = {}

channels: list = [
    "UCfITAHFPUbFwCbMYrhMJJCw",
    "UC7Jwj9fkrf1adN4fMmTkpug",
    "UCHdpnvKJDijKNe2caIasnww",
    "UCufzX8bG4LkzqKEm7J7W7UA",
    "UCbe4uwVthVsNhd7TF-mjj4A",
    "UCx6cailiCkg_mlMM7JX5yfA",
    "UC9Mu1sUuXviMxGULly4z2bg",
    "UCfSdXuFC_dnTcVA1V-aONKg",
    "UCqATHHfnvslU3Wra503Vvlw"
]

load_dotenv()
if 'y' in input("Debug? (y/N) "):
    token = getenv('DEBUGTOKEN')
else:
    token = getenv('TOKEN')
if token is None:
    print('GIMMIE YO GODDAMN TOKEN B***CH')
    exit(1)


class Video:
    def __init__(self, vid_id: str):
        ytapi = googleapiclient.discovery.build("youtube", "v3", developerKey=getenv("YTAPIKEY"))
        request = ytapi.videos().list(part="snippet", id=vid_id)
        response = request.execute()
        snippet = response["items"][0]["snippet"]
        self.id: str = response["items"][0]["id"]
        pub = parse.parse("{yyyy}-{mm}-{dd}T{HH}:{MM}:{SS}Z", snippet["publishedAt"])
        self.published_at: datetime.datetime = datetime.datetime(int(pub["yyyy"]), int(pub["mm"]), int(pub["dd"]), int(pub["HH"]), int(pub["MM"]), int(pub["SS"]))
        self.channel_id: str = snippet["channelId"]
        self.title: str = snippet["title"]
        self.channel_title: str = snippet["channelTitle"]
        self.url: str = f"https://www.youtube.com/watch?v={self.id}"


def calc_wait_time(interval: float):
    now = datetime.datetime.now()
    return interval - ((now.minute * 60 + now.second) % interval)


async def yt_checker(channel_id):
    channel = scrapetube.get_channel(channel_id)
    latest_video = None
    for video in channel:
        latest_video = video
        break
    video = Video(latest_video["videoId"])
    channel_cache = json.loads(open("youtube.json", "r").read())
    if video.channel_id not in channel_cache:
        channel_cache[video.channel_id] = {"title": "", "timestamp": ""}
    if (channel_cache[video.channel_id]["title"], channel_cache[video.channel_id]["timestamp"]) != (video.title, video.published_at.timestamp()):
        channel_cache[video.channel_id]["title"] = video.title
        channel_cache[video.channel_id]["timestamp"] = video.published_at.timestamp()
        with open(f'youtube.json', 'w') as update:
            update.write(json.dumps(channel_cache, indent=4))
        response = f'{roles[f"@{video.channel_title} Ping"].mention} New video by {video.channel_title}! `{video.title}`\n' \
            f'Uploaded <t:{int(video.published_at.timestamp())}:R>\n' \
            f'{video.url}'
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.topic is not None:
                    if 'YouTube Ping' in channel.topic:
                        await channel.send(response)
                        print(f"Sent {video.channel_title} ping!")


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
        else:

            await asyncio.sleep(calc_wait_time(300))

client.run(token)
