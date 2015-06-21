#!/usr/bin/env python

import slate
import re

with open('27_Wo_Menus_komplett_Meditx.pdf') as f:
    DOC = slate.PDF(f)

DAYS = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']


def parse_regular(text, menu_type, title):
    mud = r',* +[0-9]*\. *[a-zA-Z]* *[0-9]* *(.*) *'
    choices = {}
    for i in range(len(DAYS) - 1):
        choices[DAYS[i]] = re.sub(r'.*' + DAYS[i] + mud + DAYS[i+1] + r'.*', r'\1', text)
    return {
        'type' : menu_type,
        'title' : title,
        'choices' : choices
    }


def parse_special(text, menu_type, title):
    mud = r',* +[0-9]*\. *[a-zA-Z]* *[0-9]* *(.*?)( +[0-9]+\.[0-9]+){4} *'
    choices = {}
    for i in range(len(DAYS) - 1):
        choices[DAYS[i]] = re.sub(r'.*' + DAYS[i] + mud + r'.*', r'\1', text)
    return {
        'type' : menu_type,
        'title' : title,
        'choices' : choices
    }


menus = []
menus.append(parse_regular(DOC[0], 0, 'tages'))
menus.append(parse_regular(DOC[1], 1, 'vegetarisch'))
if len(DOC) > 2:
    menus.append(parse_special(DOC[2], 0, 'spezialitaeten'))
    

print menus
