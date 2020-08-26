from functools import (lru_cache, wraps, partial, singledispatch)


#lre_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)



#wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('decorator')
        return f(*args, **kwds)
    return wrapper


@my_decorator
def example():
    '''doc'''
    print('example')


if __name__ == "__main__":
    a = [fib(n) for n in range(20)] # классно, а самое главное быстро.
    print(a)
    example()
    print(example.__doc__, example.__name__)

    basetwo = partial(int, base=2) # полезно, но не часто используется
    print(basetwo('1110011011'))

