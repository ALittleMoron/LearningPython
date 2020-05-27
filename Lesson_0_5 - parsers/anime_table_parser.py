import requests
from bs4 import BeautifulSoup

url = "https://shikimori.one/A+Little+Moron/list/anime/order-by/rate_score"

#Используй, если в status_code выдается 403 ошибка
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

responce = requests.get(url, headers=header)
html = responce.text
souped = BeautifulSoup(html, 'html.parser')
tbody = souped.find('tbody', {'class':'entries'})
trs = tbody.find_all('tr')

string = ''
dictionary = {}

for e, tr in enumerate(trs):
    tds = tr.find_all('td')
    td_elem = tds[1].text.strip()
    
    #проверка на то, есть ли префикс "анонс" в названии аниме
    if 'анонс' in td_elem:
        td_elem = td_elem[:-5]
    name = ''.join(str(elem) for elem in td_elem)
    string += str(e+1)+'. ' + td_elem + '\n'
    dictionary.update({int(f'{e+1}'): name})

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(string)

print(dictionary)