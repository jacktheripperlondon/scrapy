from pydoc import doc
import requests

from bs4 import BeautifulSoup

youtube_url='https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

response=requests.get(youtube_url)


with open('trending.html', 'w',encoding='utf-8') as f:
    f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

vid_divs=doc.findall('div',class_='ytd-video-renderer')

print(vid_divs)