from itertools import (accumulate,chain, count, cycle,
                       combinations, combinations_with_replacement,
                       permutations, groupby, product)


if __name__ == "__main__":
    a = list(accumulate([1,2,3,4,5,6,7,8,9,10]))
    print(a, sum(range(11)), sep=' --- ')

    b = list(chain('ABC', 'DEF', 'GHI', 'JKL'))
    print(b)

    for c in count(0, 2):
        print(c)
        if c > 7:
            break

    for d in cycle([True, False, None]):
        print(d)
        if d == None:
            break

    e = list(combinations('XYZ', 2))
    print(e)

    f = list(combinations_with_replacement('XYZ', 2))
    print(f)

    g = list(permutations('XYZ', 2))
    print(g)

    h1 = [k for k, g in groupby('AAABBBCCC')]
    h2 = [list(g) for k, g in groupby('AAABBBCCC')]
    print(h1, h2, sep='\n')

    i1 = list(product('ABCD', 'xy'))
    i2 = list(product('ABCD', repeat=2))
    print(i1, i2, sep='\n')
