from bs4 import BeautifulSoup
import requests

url = 'http://www.unispital-basel.ch/das-universitaetsspital/bereiche/personal-betrieb/hotellerie/restauration/centro-centrino/'
get = requests.get(url)

soup = BeautifulSoup(get.text)

foo = soup(text=re.compile(r'KW 25'))
foo0 = foo[0]
anchor = foo0.parent
anchor.attrs['href']

pdf_url = 'http://www.unispital-basel.ch/fileadmin/unispitalbaselch/Bereiche/Personal_Betrieb/Hotellerie/Centro_Menues/25_Wo_Auswahlbuffet_Mo-Frx.pdf'

pdf = requests.get(pdf_url)

