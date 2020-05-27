import requests
from bs4 import BeautifulSoup

url = "http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html"

#Используй, если в status_code выдается 403 ошибка
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

responce = requests.get(url, headers=header)
html = responce.text
souped = BeautifulSoup(html, 'html.parser')
div = souped.find("div", {"class": "td-post-content"})
h1 = div.find_all('p')

string = ''

for i in h1:
    if i.find('strong'):
        string += i.strong.text + "\n"

with open('data.txt', 'w', encoding='utf-8') as fl:
    fl.write(string)