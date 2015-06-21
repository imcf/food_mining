import slate
import re

with open('27_Wo_Menus_komplett_Meditx.pdf') as f:
    doc = slate.PDF(f)

menu = {}

days = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']

center = r',* +[0-9]*\. *[a-zA-Z]* *[0-9]* (.*) *'

for i in range(len(days) - 1):
    menu[days[i]] = re.sub(r'.*' + days[i] + center + days[i+1] + r'.*', r'\1', doc[0])

print menu
