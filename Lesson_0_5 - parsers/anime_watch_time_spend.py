import requests
from bs4 import BeautifulSoup

url = "https://shikimori.one/A+Little+Moron/list/anime/mylist/completed/order-by/rate_score"

#Используй, если в status_code выдается 403 ошибка
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

responce = requests.get(url, headers=header)
html = responce.text
souped = BeautifulSoup(html, 'html.parser')
table = souped.find('table', {'class':'b-table list-lines'})
tbody = table.find('tbody', {'class':'entries'})
trs = tbody.find_all('tr')

ep_time = 24*60
count = 0
all_rate = 0

for tr in trs:
    tds = tr.find_all('td')
    num = tds[3].text.strip().split('/')
    rate = tds[2].text
    all_rate += int(rate)
    count += int(num[0])

print(f'{count * ep_time / 60 / 60} часов было потрачено на аниме')
print(f'{all_rate/len(trs)} - средняя моя оценка')