#!/usr/bin/env python

import os

from retrievers import retrieve_usb_menu
from parsers import parse_usb_menus, DAYS


def menu_printer(menu):
    print '--------------- ' + menu['title'] + ' ---------------'
    for day in DAYS[:-1]:
        print "%s -- %s" % (day, menu['choices'][day])
    print ''


pdf_file = retrieve_usb_menu()

menus = parse_usb_menus(pdf_file)
for menu in menus:
    menu_printer(menu)

os.remove(pdf_file)
