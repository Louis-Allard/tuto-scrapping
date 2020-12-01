import requests 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = Request('https://www.trenois.com/bosch-06019f200b-meuleuse-a-batterie-gws12v-76-article-fbc0037', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()

soup = BeautifulSoup(response, 'html.parser')
title = soup.find('title')
des = soup.find(id = 'designation')
ref = soup.find('span', class_ = 'titreprincipal_titre-declinaison')
car = soup.find('table', class_= 'table-caracteristiques')

print(title.text + '\n\n' + ref.text[1::] + '\n\n' + des.text + '\n\n' + car.text)


