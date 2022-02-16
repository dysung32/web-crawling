import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data를 받아올 사이트 주소
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# BeautifulSoup의 select 함수로 tr들 불러오기
trs = soup.select('#old_content > table > tbody > tr')

# 반복문을 통해 tr 각각 호출
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    point_tag = tr.select_one('td.point')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        point = point_tag.text
        print(rank, title, point)
