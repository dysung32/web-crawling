import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data를 받아올 사이트 주소
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# trs 불러오기
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    title_tag = tr.select_one('td.info > a.title.ellipsis')
    rank_tag = tr.select_one('td.number')
    artist_tag = tr.select_one('td.info > a.artist.ellipsis')
    title = title_tag.text.strip()
    rank = rank_tag.text[0:2].strip()
    artist = artist_tag.text
    print(rank, title, artist)