import requests
import re
import googleapiclient.discovery
import datetime
from dotenv import load_dotenv
from os import getenv

load_dotenv()
yt_key = getenv('YTAPIKEY')
if yt_key is None:
    print("Requires a YouTube Data API key")
    exit(1)

class YTVideo:
    def __init__(self, title, url, time, channel):
        self.title = title
        self.url = url
        self.published = time
        self.channel = channel


def get_latest_video(channel_handle: str):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=yt_key)

    channel = f"https://www.youtube.com/{channel_handle}"

    html = requests.get(channel + "/videos").text
    vid_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

    get_info = youtube.videos().list(part="snippet", id=re.search('(?<="videoId":").*?(?=")', html).group())
    response = get_info.execute()

    vid_title = response['items'][0]['snippet']['title']
    vid_channel = response['items'][0]['snippet']['channelTitle']
    vid_time = response['items'][0]['snippet']['publishedAt']
    vid_time_year = int(vid_time[:4])
    vid_time_month = int(vid_time[5:7])
    vid_time_day = int(vid_time[8:10])
    vid_time_hour = int(vid_time[11:13])
    vid_time_minute = int(vid_time[14:16])
    vid_time_second = int(vid_time[17:19])
    vid_time = datetime.datetime(vid_time_year,
                                 vid_time_month,
                                 vid_time_day,
                                 vid_time_hour,
                                 vid_time_minute,
                                 vid_time_second)

    return YTVideo(vid_title, vid_url, vid_time, vid_channel)
