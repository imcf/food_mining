#!/usr/bin/env python

import re
import os

from bs4 import BeautifulSoup
from requests import get
from urllib import urlretrieve
from tempfile import mkstemp
from datetime import datetime


def retrieve_usb_menu():
    woty = str(datetime.utcnow().isocalendar()[1])  # week of the year

    base = 'http://www.unispital-basel.ch'
    url = base + '/das-universitaetsspital/bereiche/personal-betrieb/hotellerie/restauration/centro-centrino/'
    response = get(url)

    soup = BeautifulSoup(response.text)

    menu_links = soup(text=re.compile(r'KW ' + woty))
    # menu_links[0] contains the buffet, menu_links[1] the standard menus:
    pdf_url = base + menu_links[1].parent.attrs['href']
    # print pdf_url

    fd, pdf_file = mkstemp()
    urlretrieve(pdf_url, pdf_file)
    os.close(fd)
    return pdf_file

