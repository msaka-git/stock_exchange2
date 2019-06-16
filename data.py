# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

url = "http://finans.mynet.com/borsa/hisseler/"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
print(response)
a = input("Hisse adı giriniz:")
a=a.upper()

hisse_adi=soup.find_all("td",{"class":"ndt-leftText ndt-noBorderRight"})
#print(hisse_adi)

if a in hisse_adi:
    print(hisse_adi)

#for ad in hisse_adi:
#    hisse_adi=ad.text



url_fiyat="http://finans.mynet.com/borsa/hisseler/acsel-acipayam-seluloz"
response_fiyat=requests.get(url_fiyat)

html_fiyat_icerigi = response_fiyat.content
soup_fiyat=BeautifulSoup(html_fiyat_icerigi,"html.parser")

#hisse_fiyati = soup_fiyat.find_all("span",{"class":"dtColTwo"})

#print(hisse_fiyati[0].text)

##### sadece linki almak
links = []
for tag in soup.find_all('td', {'class' : 'ndt-leftText ndt-noBorderRight'}):
    for anchor in tag.find_all('a'):
        links.append(anchor['href'])


a = input("Hisse girin: ")


for hisse in links:
    url_fiyat = "http://finans.mynet.com/" + hisse


    if a in url_fiyat:
        print(url_fiyat)
        response_fiyat = requests.get(url_fiyat)

        html_fiyat_icerigi = response_fiyat.content
        soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

        hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

        hisse_fiyati = hisse_fiyati[0].text
        print(hisse_fiyati)





#######


#basliklar = soup.find_all("td",{"class":"titleColumn"})
#ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})
#for i in hisse_adi:
#    print(i.text)




