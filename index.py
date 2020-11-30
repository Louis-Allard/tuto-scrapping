import requests 
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    tds = soup.findAll('span', class_ = 'mw-headline')
    
    [print(str(td.text) + '\n') for td in tds]
else:
    print('Erreur de response : ' + str(response))