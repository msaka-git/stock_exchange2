# -*- coding: utf-8 -*-

import requests
import datetime

from bs4 import BeautifulSoup

class hisse_properties():
    def __init__(self,hisse_adi,hisse_fiyat,hisse_fk,hisse_eps,hisse_peg,peg_yillik,peg_5yillik,hisse_pd_dd,base_growth_rate,base_growth_rate5y,
                 base_growth_rate10y,fair_value,yorum):
        self.hisse_adi=hisse_adi
        self.hisse_fiyat=hisse_fiyat
        self.hisse_fk=hisse_fk

        self.hisse_eps=hisse_eps
        self.hisse_peg=hisse_peg
        self.peg_5yillik=peg_5yillik
        self.peg_yillik=peg_yillik
        self.hisse_pd_dd=hisse_pd_dd
        self.base_growth_rate=base_growth_rate
        self.base_growth_rate5y=base_growth_rate5y
        self.base_growth_rate10y=base_growth_rate10y
        self.fair_value=fair_value
        self.yorum=yorum

    def __str__(self):
        return "Hisse adı: {}\nGüncel fiyat: {}\nHisse fiyat-kazanç: {}\nHisse EPS: {}\nPEG Güncel: {}\nPEG Yıllık: {}\nPEG 5 yıllık: {}\nHisse piyasa/defter oranı: {}\n" \
               "Büyüme Oranı (% 1,5,10 yıllık yüzde): {} | {} | {}\nFair Value: {}\n\nYorum: {}".format(
            self.hisse_adi,self.hisse_fiyat,self.hisse_fk,self.hisse_eps,self.hisse_peg,self.peg_yillik,self.peg_5yillik,self.hisse_pd_dd,self.base_growth_rate,
        self.base_growth_rate5y,self.base_growth_rate10y,self.fair_value,self.yorum)



class hisse():
    def __init__(self):
        self.hisse_adi()

    def query(self):
        url_isbank = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/sayfalar/sirket-karti.aspx?hisse={}".format(
            self.a.upper())

        response_isbank = requests.get(url_isbank)
        html_icerigi_isbank = response_isbank.content
        self.soup_isbank = BeautifulSoup(html_icerigi_isbank, "html.parser")

        ####
        url_bgundem="https://www.borsagundem.com/piyasa-ekrani/hisse-detay/{}".format(self.a.upper())
        response_bgundem=requests.get(url_bgundem)
        html_icerigi_bgundem=response_bgundem.content
        self.soup_bgundem=BeautifulSoup(html_icerigi_bgundem,"html.parser")


    def hisse_adi(self):
        self.a=input("Hisse adı girin: ")


    def fiyat_sorgula(self):
        year = datetime.datetime.now()
        year1 = year.year - 1
        year2 = year.year - 2

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
        links_ce = []
        links_fj = []
        links_kq = []
        links_rz = []

        for tag in soup.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag.find_all('a'):
                links.append(anchor['href'])

        for tag_ce in soup_ce.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_ce.find_all('a'):
                links_ce.append(anchor['href'])

        for tag_fj in soup_fj.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
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
            self.url_fiyat_gwrate=url_fiyat + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2=url_fiyat + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            self.url_fiyat_info=url_fiyat + "sirket-bilgileri"
            if self.a in url_fiyat:

                response_fiyat = requests.get(url_fiyat)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                return self.my_float


        for h_ce in links_ce:
            url_fiyat_ce = "http://finans.mynet.com/" + h_ce
            self.url_fiyat_gwrate = url_fiyat_ce + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_ce + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            self.url_fiyat_info = url_fiyat_ce + "sirket-bilgileri"
            if self.a in url_fiyat_ce:
                response_fiyat = requests.get(url_fiyat_ce)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                return self.my_float

        for h_fj in links_fj:
            url_fiyat_fj = "http://finans.mynet.com/" + h_fj
            self.url_fiyat_gwrate = url_fiyat_fj + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_fj + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            self.url_fiyat_info = url_fiyat_fj + "sirket-bilgileri"
            if self.a in url_fiyat_fj:
                response_fiyat = requests.get(url_fiyat_fj)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")
                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                return self.my_float


        for h_kq in links_kq:
            url_fiyat_kq = "http://finans.mynet.com/" + h_kq
            self.url_fiyat_gwrate = url_fiyat_kq + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_kq + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            self.url_fiyat_info = url_fiyat_kq + "sirket-bilgileri"
            if self.a in url_fiyat_kq:

                response_fiyat = requests.get(url_fiyat_kq)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                return self.my_float

        for h_rz in links_rz:
            url_fiyat_rz = "http://finans.mynet.com/" + h_rz
            self.url_fiyat_gwrate = url_fiyat_rz + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_rz + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            self.url_fiyat_info = url_fiyat_rz + "sirket-bilgileri"
            if self.a in url_fiyat_rz:

                response_fiyat = requests.get(url_fiyat_rz)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                return self.my_float

    def fiyat_kazanc(self):
        self.query()
        #self.hisse_fk=self.soup_isbank.select_one('th:contains("F/K") + td').text
        #hisse_fk=self.soup_isbank.find_all('div', {'id': 'ozetFinansalGostergeler1'})
        hisse_fk=self.soup_bgundem.select_one('p:contains("FK") + span').text

        h_fk = hisse_fk.replace(',', '.')
        h_fk = float(h_fk)
        self.my_float_fk = h_fk
        return self.my_float_fk


    def eps(self):
        self.fiyat_sorgula()
        self.query()
        response_fiyat = requests.get(self.url_fiyat_info)
        html_content_fiyat = response_fiyat.content
        soup_finans = BeautifulSoup(html_content_fiyat, "html.parser")

        self.hisse_adet = soup_finans.select_one('span:contains("Piyasa Değeri") + span').text
        string = self.hisse_adet[:-2]

        h_adeti = string.replace(',', '.')

        my_string_e = h_adeti
        commas_removed_e = my_string_e.replace('.', '')  # remove comma separation
        self.my_float_e = float(commas_removed_e)  # turn from string to float. Share amount.


        #### NET Donem Kari ######
        urlkar = "https://yatirim.akbank.com/tr-tr/hisse-senedi/Sayfalar/hisse-senet-detay.aspx?hisse=" + self.a
        response_kar = requests.get(urlkar)
        html_content_kar = response_kar.content
        soup_kar = BeautifulSoup(html_content_kar, "html.parser")
        #kar = soup_kar.select_one('td:contains("- Ana Ortaklık Payları") + td + td').text
        kar = soup_kar.select_one('td:contains("Net Dönem Karı/Zararı") + td').text

        h_kar = kar.replace(',', '.')
        commas_removed_kar = h_kar.replace('.', '')
        self.my_float_kar = float(commas_removed_kar)

        ##### Shares in circulation #######
        self.hisse_tedavul=self.my_float_e / self.my_float
        self.hisse_eps=round((self.my_float_kar / self.hisse_tedavul),2)
        return self.hisse_eps

    def pd_dd(self):
        self.query()
        #self.hisse_pd_dd = self.soup_isbank.select_one('th:contains("PD/DD") + td').text
        #hisse_pd_dd=self.soup_isbank.find_all('div', {'id': 'ozetFinansalGostergeler1'})
        hisse_pd_dd=self.soup_bgundem.select_one('p:contains("PD/DD") + span').text

        h_pddd = hisse_pd_dd.replace(',', '.')
        h_pddd = float(h_pddd)

        self.my_float_pd_dd = h_pddd
        return self.my_float_pd_dd

    def peg_calcul(self):

        self.peg=round(self.my_float_fk / self.hisse_eps,2)
        return self.peg


    def base_growth_rate(self):

        try:
            response_gr1 = requests.get(self.url_fiyat_gwrate)
            html_fiyat_icerigi1 = response_gr1.content
            soup_fiyat1 = BeautifulSoup(html_fiyat_icerigi1, "html.parser")
            hisse_fiyati1 = soup_fiyat1.find_all("td", {"data-title-value": "Net Dönem Karı/Zararı_1"})
            hisse_fiyati1 = hisse_fiyati1[0].text
            my_string1 = hisse_fiyati1
            commas_removed1 = my_string1.replace(',', '.')  # remove comma separation
            self.my_float_gr1 = float(commas_removed1)  # turn from string to float.

            response_gr2 = requests.get(self.url_fiyat_gwrate2)
            html_fiyat_icerigi2 = response_gr2.content
            soup_fiyat2 = BeautifulSoup(html_fiyat_icerigi2, "html.parser")
            hisse_fiyati2 = soup_fiyat2.find_all("td", {"data-title-value": "Net Dönem Karı/Zararı_1"})
            hisse_fiyati2 = hisse_fiyati2[0].text
            my_string2 = hisse_fiyati2
            commas_removed2 = my_string2.replace(',', '.')  # remove comma separation
            self.my_float_gr2 = float(commas_removed2)  # turn from string to float.

            self.gw=(self.my_float_gr1 - self.my_float_gr2) / self.my_float_gr2
            self.gw=round(self.gw * 100,2)
            return self.gw

        except IndexError:
            self.gw="Eksi değer veya geçersiz değer"
            return self.gw

    def base_growth_rate5y(self):

        try:
            self.gw_5years = self.my_float_gr1 / self.my_float_gr2
            self.gw_5years_kuvvet = (self.gw_5years ** 0.2) - 1
            self.gw_5years_yuzde = round(self.gw_5years_kuvvet * 100,2)

            return self.gw_5years_yuzde
        except AttributeError:
            self.gw_5years_yuzde = "Eksi değer veya geçersiz değer"
            return self.gw_5years_yuzde

    def base_growth_rate10y(self):

        try:
            self.gw_10years_kuvvet=(self.gw_5years ** 0.1) - 1
            self.gw_10years_yuzde=round(self.gw_10years_kuvvet * 100,2)
            return self.gw_10years_yuzde
        except AttributeError:
            self.gw_10years_yuzde = "Eksi değer veya geçersiz değer"
            return self.gw_10years_yuzde

    def peg_yearly(self):
        try:
            self.gw_rate=(self.my_float_gr1 - self.my_float_gr2) / self.my_float_gr2
            self.gw_rate=self.gw_rate * 100
            self.peg_yearly=round(self.my_float_fk / self.gw_rate,2)
            return self.peg_yearly
        except AttributeError:
            self.peg_yearly="Dönem kar veya zararı bulunamadı."
            return self.peg_yearly

    def peg_5years(self):
        try:
            self.gw_5years = self.my_float_gr1 / self.my_float_gr2
            self.gw_5years_rate = (self.gw_5years ** 0.2) - 1
            self.gw_5years_yuzde = round(self.gw_5years_kuvvet * 100, 2)
            self.peg_5y = round(self.my_float_fk / self.gw_5years_yuzde,2)
            return self.peg_5y
        except AttributeError:
            self.peg_yearly="Dönem kar veya zararı bulunamadı."
            return self.peg_yearly



    def fair_value(self):
        try:
            self.fv=round(self.gw * self.hisse_eps,2)
            return self.fv
        except TypeError:
            self.fv="Veri bulunamadı."
            return self.fv

    def yorum_hisse(self):
        try:
            if (self.gw > float(0)) and (self.gw <= float(30)):
                if (self.fv < self.my_float) and (self.peg_yearly < float(1)) and (self.my_float_pd_dd < float(1)) and \
                    (self.peg_5y < float(1)):
                    return "Hissenin FV'si güncel fiyatından düşük, fiyat ucuz.\nYıllık PEG 1'den düşük\nPiyasa değeri defter değerinden düşük.\n" \
                       "5 yıllık PEG de 1'den düşük\nSanırım çok ucuz bir hisse yakaladın: Sonuç ÇOK OLUMLU."
                elif (self.fv < self.my_float) and (self.peg_yearly < float(1)) and (self.my_float_pd_dd < float(1)):
                    return "Hissenin FV'si güncel fiyatından düşük, fiyat ucuz.\nPiyasa değeri defter değerinden düşük.\n" \
                           "Yıllık PEG 1'den düşük. Fakat 5 yıllık PEG fazla: OLUMLU."
                elif (self.peg_yearly < float(1)) and (self.my_float_pd_dd < float(1)):
                    return "PEG ve pd/dd olması gerekenin altında.\nYıllık bazda hisse makul gibi gözüküyor. Fair Value'ye (Adil fiyat).\n" \
                           "Ayrıca şu anda hisse fiyatı {}'nın altında mı?.\nSonuç: Yıllık olarak makul gibi. Teknik analiz lazım.".format(self.hisse_eps * self.my_float_fk)
                elif (self.gw > self.my_float_fk):
                    return "Büyüme oranı şu anki fiyat kazançtan yüksek. Bu çok olumlu.\nDiğer indikatörlere bak.\n" \
                           "Teknik analiz yap. Büyüme oranları çok fahiş olmamalı.\nFiyat karşılaştırması yaparken geçmiş verileri incele.\n" \
                           "Sonuç: Potansiyel var ama RISK büyük."

                else:
                    return "Fiyatın ucuz olduğuna dair olumlu bir gösterge bulamadım."

            else:
                return "Büyüme oranı yüzde 30'in üstünde veya değerler ekside.\nHesaplama gerçeği yansıtmıyor."

        except TypeError:
            return "Veri bulunamadı."

    def menu(self):
        self.fiyat_sorgula()
        self.fiyat_kazanc()
        self.eps()
        self.peg_calcul()
        self.pd_dd()
        self.base_growth_rate()
        self.base_growth_rate5y()
        self.base_growth_rate10y()
        self.peg_yearly()
        self.peg_5years()
        self.fair_value()
        self.yorum_hisse()
        try:
            sonuc=hisse_properties(self.a,self.my_float,self.my_float_fk,self.hisse_eps,self.peg,self.peg_yearly,self.peg_5y,self.my_float_pd_dd,self.gw,
                                   self.gw_5years_yuzde,self.gw_10years_yuzde,self.fv,self.yorum_hisse())
            print(sonuc)
        except AttributeError:
            print("Bazı veriler bulunamadı.")



Hisse=hisse()
Hisse.menu()


