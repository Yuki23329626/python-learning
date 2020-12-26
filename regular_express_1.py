import string
import re

url = 'setnmh.com/series-lvcnh-561042-1-無良公會'

head = [m.start() for m in re.finditer('-', url)][-2] + 1
tail = [m.start() for m in re.finditer('-', url)][-1]
page = 30

print( url[:head] + str(page) + url[tail:])