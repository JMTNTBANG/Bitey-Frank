import requests
import re
import googleapiclient.discovery
import datetime

class ytVideo():
    def __init__(self, vidTitle, vidUrl, vidTime, vidChannel):
        self.title = vidTitle
        self.url = vidUrl
        self.published = vidTime
        self.channel = vidChannel


def getLatestVideo(channelHandle:str):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey = 'AIzaSyBP-99NKZanXgXFhymYq-5unmmXTNJ94Yk')

    channel = f"https://www.youtube.com/{channelHandle}"

    html = requests.get(channel + "/videos").text
    vidUrl = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group() #type: ignore

    getInfo = youtube.videos().list(part="snippet",id=re.search('(?<="videoId":").*?(?=")', html).group()) #type: ignore
    response = getInfo.execute()

    vidTitle = response['items'][0]['snippet']['title']
    vidChannel = response['items'][0]['snippet']['channelTitle']
    vidTime = response['items'][0]['snippet']['publishedAt']
    vidTimeYear = int(vidTime[:4])
    vidTimeMonth = int(vidTime[5:7])
    vidTimeDay = int(vidTime[8:10])
    vidTimeHour = int(vidTime[11:13])
    vidTimeMinute = int(vidTime[14:16])
    vidTimeSecond = int(vidTime[17:19])
    vidTime = datetime.datetime(vidTimeYear,vidTimeMonth,vidTimeDay,vidTimeHour,vidTimeMinute,vidTimeSecond)

    return ytVideo(vidTitle, vidUrl, vidTime, vidChannel)