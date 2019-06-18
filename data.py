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

url_fiyat="http://finans.mynet.com/borsa/hisseler/acsel-acipayam-seluloz/"
response_fiyat=requests.get(url_fiyat)
html_fiyat_icerigi = response_fiyat.content
soup_fiyat=BeautifulSoup(html_fiyat_icerigi,"html.parser")

hisse_fiyati = soup_fiyat.find("span",{"class":"dtColTwo"})
print(response_fiyat)
#basliklar = soup.find_all("td",{"class":"titleColumn"})
#ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})
#for i in hisse_adi:
#    print(i.text)

for f in hisse_fiyati:

    print(f)
