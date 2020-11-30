import requests 
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde'

response = requests.get(url)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, 'html.parser')
    tds = soup.findAll('td')
    for td in tds:
        a = td.find('a')
        link = a['href']
        links.append('https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde' + link)

    print(links)