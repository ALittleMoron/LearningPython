import re


# greed and nogreed Regex
amansas = re.compile(r'\s<[^o].*>') #nogreed
ask = amansas.search(' <object <abs.txt> in 0x215fa12> is no longer available')
print(ask.group())

amansas = re.compile(r'\s<[^o].*?>') #greed
ask = amansas.search(' <object <abs.txt> in 0x215fa12> is no longer available')
print(ask.group())