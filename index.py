import requests 
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde'

response = requests.get(url)

if response.ok:
    print(response.text)