from collections import (Counter, deque, defaultdict, OrderedDict, namedtuple)


if __name__ == '__main__':
    shop = Counter()
    for food in ['apple', 'orange', 'apple', 'ice cream', 'apple', 'orange']:
        shop[food] += 1
    print(shop, sorted(shop.elements()))
    print(shop.most_common(1))
    del shop

    piramide = deque()
    for el in [2,3,4,5,6]:
        piramide.append(el)
    piramide.appendleft(1)
    print(piramide)
    piramide.pop()
    piramide.popleft()
    print(piramide)
    del piramide

    defdict = defaultdict()
    print(defaultdict)
    for el in range(5):
        defdict[el] = el+10
    print(defdict)

    odict = OrderedDict(defdict)
    print(odict.values(), odict.items())
    odict = OrderedDict(sorted(defdict.items(), reverse=True))
    print(odict)
    del defdict, odict

    author = namedtuple('author', ['first_name', 'last_name'])
    a = author('Lev', 'Tolstoy')
    print(a, a.first_name, a.last_name)
    da = a._asdict()
    fa = a._fields
    print(type(da), type(fa), type(a))
    x,y = a
    print(x,y)
    vals = ['Aleksandr', 'Pushkin']
    a_p = author._make(vals)
    print(a_p)
