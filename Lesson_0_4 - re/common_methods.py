import re


# search
# greed and nogreed Regex
def greed():
    x = re.compile(r'\s<[^o].*>') #nogreed
    y = x.search(' <object <abs.txt> in 0x215fa12> is no longer available')
    print(y.group())

    x = re.compile(r'\s<[^o].*?>') #greed
    y = x.search(' <object <abs.txt> in 0x215fa12> is no longer available')
    print(y.group())


# find all
def fl():
    x = re.compile(r'\+\d{1,3}\(\d{3}\)\d{3}-\d{2}-\d{2}')
    y = x.findall('+162(152)251-25-25 +7(918)873-93-93 +11(111)1111111')
    print(y)


# match
def mch():
    x = re.compile(r'\d{0,10}')
    y = x.match('124 methods')
    print(y.group()) # or group(number) number = 1,...,n


if __name__ == "__main__":
    pass