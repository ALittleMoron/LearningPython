def yield_from_range_generator(n:int):
    yield from range(n)


def super_yield_from_generator(n:int ,x:list):
    yield from (str(z) for z in x)
    yield from yield_from_range_generator(n)
    yield ' final!'


if __name__ == "__main__":
    a = super_yield_from_generator(25, [25,1,2,5])
    print(list(a))
