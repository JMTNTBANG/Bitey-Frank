import requests
import re
import googleapiclient.discovery

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey = 'AIzaSyBP-99NKZanXgXFhymYq-5unmmXTNJ94Yk')

channel = "https://www.youtube.com/@DankPods"

html = requests.get(channel + "/videos").text
info = re.search('(?<={"label":").*?(?="})', html).group()
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

getInfo = youtube.videos().list(part="snippet",id=re.search('(?<="videoId":").*?(?=")', html).group())
response = getInfo.execute()

print(response['items'][0]['snippet']['title'])
# print(info.find('by DankPods'))
# vidName = info[:info.find('by DankPods')-1]

# print(vidName)

# print(info)
# print(url)