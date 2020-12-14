import requests 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import mysql.connector
from data import HOST, USER, PASSWORD, DATABASE, URL

bdd = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)

curseur = bdd.cursor()

for i in range(0,90):    
    print('Page ' + str(i))
    url = Request(URL + str(i), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()      

    soup = BeautifulSoup(response, 'html.parser')

    title = soup.find('title')
    
    des = soup.find(id = 'designation')
    ref = soup.find('span', class_ = 'titreprincipal_titre-declinaison')
    car = soup.find('table', class_= 'table-caracteristiques')
    
    if len(title)!=0:  
        curseur.execute("INSERT INTO produits(REF, TITLE, DESCR, CARACT) VALUES (%s, %s, %s, %s)", (ref.text[12::], title.text, des.text, car.text ))
        bdd.commit()
    else:
        print("Pas de page produit")  

bdd.close()

print(bdd)
print("=================== END ===================")
