import requests

from bs4 import BeautifulSoup


a="sahol"

#url_bank = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/sayfalar/sirket-karti.aspx?hisse={}".format(a.upper())
url_bank="https://www.borsagundem.com/piyasa-ekrani/hisse-detay/{}".format(a.upper())
response_bank = requests.get(url_bank)
html_content_bank = response_bank.content
soup_bank = BeautifulSoup(html_content_bank, "html.parser")
#pd_dd=soup_bank.select_one('th:contains("PD/DD") + td').text # This is between td tag. it's called "adjacent sibling td"
#commas_removed_pd_dd = pd_dd.replace(',', '.')  # remove comma separation
#my_float_pd_dd = float(commas_removed_pd_dd)
#print(my_float_pd_dd)

print(url_bank)
de=soup_bank.select_one('p:contains("FK") + span').text
h_fk = de.replace(',', '.')
h_fk=float(h_fk)
print(h_fk)

cv=soup_bank.select_one('p:contains("PD/DD") + span').text
#print(cv)

pd=soup_bank.find_all('div', {'id': 'ozetFinansalGostergeler1'})

links=[]
for i in pd:

    rows = i.findAll('td')
    a=rows[-1].text
    h_pd = a.replace(',', '.')
    a=float(h_pd)

#print(type(a))
#print(a)

for z in pd:
    r=z.findAll('td')
    fk=r[-2].text
    h_fk = fk.replace(',', '.')
    fk=float(h_fk)
#print(fk)

'''
fk=soup_bank.select_one('th:contains("F/K") + td').text
c=soup_bank.select_one('.vertical table:not([class]) tr:nth-of-type(3) td:nth-of-type(1)').text


#print(c)

d=soup_bank.select_one('.vertical table:not([class]) tr:nth-of-type(3) td').text
#print(d)

#fk = f.text
my_string_fk = fk
commas_removed_fk = my_string_fk.replace(',', '.')  # remove comma separation
my_float_fk = float(commas_removed_fk)
print(my_float_fk)
print(type(my_float_fk))




url_fiyat_info="http://finans.mynet.com/borsa/hisseler/sahol-sabanci-holding/sirket-bilgileri/"
response_fiyat = requests.get(url_fiyat_info)

html_content_fiyat = response_fiyat.content
soup_finans = BeautifulSoup(html_content_fiyat, "html.parser")
#adet=soup_finans.find_all('span', {'class': 'dtColOne'})
deger=soup_finans.select_one('span:contains("Piyasa Değeri") + span').text
string=deger[:-2]

h_adeti = string.replace(',', '.')

my_string_e = h_adeti
commas_removed_e = my_string_e.replace('.', '')  # remove comma separation
#print(commas_removed_e)
my_float_e = float(commas_removed_e)  # turn from string to float.
my_float_e=my_float_e/100
print(my_float_e)
############################ NET DONEM KARI #############################################
urlkar="https://yatirim.akbank.com/tr-tr/hisse-senedi/Sayfalar/hisse-senet-detay.aspx?hisse=SAHOL"
response_kar=requests.get(urlkar)
html_content_kar=response_kar.content
soup_kar=BeautifulSoup(html_content_kar,"html.parser")
kar=soup_kar.select_one('td:contains("- Ana Ortaklık Payları") + td + td').text

h_kar=kar.replace(',','.')

commas_removed_kar=h_kar.replace('.','')
my_float_kar=float(commas_removed_kar)
my_float_kar=my_float_kar / 100
print("Net kar: "+str(my_float_kar))

####
eps=round((my_float_kar / my_float_e),2)
#print(eps)
f=my_float_e / 9.60 # piyasa degerinin hisse fiyatina bolunmesi
print("tedavuldeki hisse : {}".format(f))
fi=my_float_kar/f

fir=round((my_float_kar/f),2)
print(fir)
'''