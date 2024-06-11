import discord
import asyncio
import json
import scrapetube
import googleapiclient.discovery
import parse
from pytz import timezone
from datetime import datetime, timedelta, time

# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)
schedule = None
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


class Config:
    def __init__(self):
        with open("./src/config.json", "r") as raw_config:
            raw_config = json.loads(raw_config.read())
            self.token = raw_config["token"]
            self.ytapitoken = raw_config["ytApiToken"]
            self.guildId = raw_config["guildId"]
            self.youtubePingChannel = raw_config["specialChannels"]["youtube_ping"]
            self.scheduleChannel = raw_config["specialChannels"]["schedule"]


config = Config()


class Video:
    def __init__(self, vid_id: str):
        ytapi = googleapiclient.discovery.build("youtube", "v3", developerKey=config.ytapitoken)
        request = ytapi.videos().list(part="snippet", id=vid_id)
        response = request.execute()
        snippet = response["items"][0]["snippet"]
        self.id: str = response["items"][0]["id"]
        pub = parse.parse("{yyyy}-{mm}-{dd}T{HH}:{MM}:{SS}Z", snippet["publishedAt"])
        self.published_at: datetime = datetime(int(pub["yyyy"]), int(pub["mm"]), int(pub["dd"]), int(pub["HH"]), int(pub["MM"]), int(pub["SS"]))
        self.channel_id: str = snippet["channelId"]
        self.title: str = snippet["title"]
        self.channel_title: str = snippet["channelTitle"]
        self.url: str = f"https://www.youtube.com/watch?v={self.id}"


def calc_wait_time(interval: float):
    now = datetime.now()
    return interval - ((now.minute * 60 + now.second) % interval)


async def yt_checker(channel_id):
    channel = scrapetube.get_channel(channel_id, limit=1)
    latest_video = None
    for video in channel:
        latest_video = video
        break
    if latest_video is None:
        return
    video = Video(latest_video["videoId"])
    channel_cache = json.loads(open("./src/youtube.json", "r").read())
    if video.channel_id not in channel_cache:
        channel_cache[video.channel_id] = {"title": "", "timestamp": ""}
    if (channel_cache[video.channel_id]["title"], channel_cache[video.channel_id]["timestamp"]) != (video.title, video.published_at.timestamp()):
        channel_cache[video.channel_id]["title"] = video.title
        channel_cache[video.channel_id]["timestamp"] = video.published_at.timestamp()
        with open(f'./src/youtube.json', 'w') as update:
            update.write(json.dumps(channel_cache, indent=4))
        response = f'{roles[f"@{video.channel_title} Ping"].mention} New video by {video.channel_title}! `{video.title}`\n' \
            f'Uploaded <t:{int(video.published_at.timestamp())}:R>\n' \
            f'{video.url}'
        channel = await client.fetch_channel(config.youtubePingChannel)
        await channel.send(response)
        print(f"Sent {video.channel_title} ping!")


async def goob_schedule_upd():
    aussie_timezone = timezone("Australia/Adelaide")
    aussie_date = datetime.now(aussie_timezone)
    global schedule
    this_week = {}
    for day in range(5):
        this_week[day] = aussie_date + timedelta(days=-aussie_date.weekday() + day,
                                                 weeks=0,
                                                 hours=-aussie_date.hour + 9,
                                                 minutes=-aussie_date.minute,
                                                 seconds=-aussie_date.second,
                                                 microseconds=-aussie_date.microsecond)
    if schedule != this_week:
        schedule = this_week
        channel = await client.fetch_channel(config.scheduleChannel)
        await channel.purge()
        schedule_message = (("||                                                                                            ||\n"
                            "> ## Monday: <t:{0}:d> <t:{0}:t> (<t:{0}:R>)\n"
                            "> ## Tuesday: <t:{1}:d> <t:{1}:t> (<t:{1}:R>)\n"
                            "> ## Wednesday: <t:{2}:d> <t:{2}:t> (<t:{2}:R>)\n"
                            "> ## Thursday: <t:{3}:d> <t:{3}:t> (<t:{3}:R>)\n"
                            "> ## Friday: <t:{4}:d> <t:{4}:t> (<t:{4}:R>)\n"
                            "||                                                                                            ||"
                             ).format(this_week[0].timestamp().__round__(),
                                      this_week[1].timestamp().__round__(),
                                      this_week[2].timestamp().__round__(),
                                      this_week[3].timestamp().__round__(),
                                      this_week[4].timestamp().__round__()))
        await channel.send(schedule_message)


@client.event
async def on_ready():
    for guild in client.guilds:
        for role in guild.roles:
            roles[f'@{role.name}'] = role

    while True:
        await goob_schedule_upd()
        for channel in channels:
            await (yt_checker(channel))
            await asyncio.sleep(calc_wait_time(60))

client.run(config.token)
