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
        url_ce="http://finans.mynet.com/borsa/hisseler/c-e/"
        url_fj = "http://finans.mynet.com/borsa/hisseler/f-j/"
        url_kq = "http://finans.mynet.com/borsa/hisseler/k-q/"
        url_rz = "http://finans.mynet.com/borsa/hisseler/r-z/"

        response = requests.get(url)
        response_ce=requests.get(url_ce)
        response_fj = requests.get(url_fj)
        response_kq = requests.get(url_kq)
        response_rz = requests.get(url_rz)

        html_icerigi_ce=response_ce.content
        html_icerigi_fj = response_fj.content
        html_icerigi_kq = response_kq.content
        html_icerigi_rz = response_rz.content
        html_icerigi = response.content

        soup_ce=BeautifulSoup(html_icerigi_ce,"html.parser")
        soup_fj = BeautifulSoup(html_icerigi_fj, "html.parser")
        soup_kq = BeautifulSoup(html_icerigi_kq, "html.parser")
        soup_rz = BeautifulSoup(html_icerigi_rz, "html.parser")

        soup = BeautifulSoup(html_icerigi, "html.parser")
        links = []
        links_ce= []
        links_fj = []
        links_kq = []
        links_rz = []

        for tag in soup.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag.find_all('a'):
                links.append(anchor['href'])

        for tag_ce in soup_ce.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_ce.find_all('a'):
                links_ce.append(anchor['href'])

        for tag_fj in soup_ce.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_fj.find_all('a'):
                links_fj.append(anchor['href'])

        for tag_kq in soup_kq.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_kq.find_all('a'):
                links_kq.append(anchor['href'])

        for tag_rz in soup_rz.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_rz.find_all('a'):
                links_rz.append(anchor['href'])

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

        for h_ce in links_ce:
            url_fiyat_ce = "http://finans.mynet.com/" + h_ce

            if self.a in url_fiyat_ce:

                    print(url_fiyat_ce)
                    response_fiyat = requests.get(url_fiyat_ce)

                    html_fiyat_icerigi = response_fiyat.content
                    soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                    hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                    hisse_fiyati = hisse_fiyati[0].text
                    print(hisse_fiyati)





Hisse=hisse()
Hisse.fiyat_sorgula()