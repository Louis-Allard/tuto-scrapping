import requests 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

for i in range(0,40):    
    print('Page ' + str(i))
    url = Request('https://www.trenois.com/bosch-06019f200b-meuleuse-a-batterie-gws12v-76-article-fbc00' + str(i), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()      

    soup = BeautifulSoup(response, 'html.parser')

    title = soup.find('title')
    
    des = soup.find(id = 'designation')
    ref = soup.find('span', class_ = 'titreprincipal_titre-declinaison')
    car = soup.find('table', class_= 'table-caracteristiques')
    
    if len(title)!=0:  
        print(title.text + '\n\n' + ref.text[1::] + '\n\n' + des.text + '\n\n' + car.text)
    else:
        print("Pas de page produit")