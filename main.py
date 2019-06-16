# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

class hisse():
    def __init__(self):
        self.hisse_adi()


    def hisse_adi(self):
        self.a=input("Hisse adı girin: ")


    def fiyat_sorgula(self):
        url = "http://finans.mynet.com/borsa/hisseler/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        links = []

        for tag in soup.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag.find_all('a'):
                links.append(anchor['href'])


        for h in links:
            url_fiyat = "http://finans.mynet.com/" + h

            if self.a in url_fiyat:
                print(url_fiyat)
                response_fiyat = requests.get(url_fiyat)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                print(hisse_fiyati)

Hisse=hisse()
Hisse.fiyat_sorgula()