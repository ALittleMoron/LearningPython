# Тест алгоритмов поиска и их скорости

from time import monotonic
from random import randint, choice

# переменные
iterable = list # для наглядности. А так, можно и tuple, и set.
all_types = type
element_position = int


def benchmark(func):
    """ декоратор, проверяющий время работы функции """
    def wrapper(*args, **kwargs):
        start = monotonic()
        r_v = func(*args, **kwargs)
        end = monotonic()
        print(f'{func.__name__}: {end - start} секунд')
        return r_v
    return wrapper


@benchmark
def lineal_search(seq:iterable, element:all_types) -> element_position:
    """ Алгоритм линейного поиска в последовательности

    аргументы:
    seq -- последовательность, в которой будет вестись поиск
    element -- элемент, который нужно найти

    возвращает element_position -- номер позиции элемента (начиная с нуля)
    """
    for item in range(len(seq)):
        if seq[item] == element:
            return item
    return -1


@benchmark
def binary_search(seq:iterable, element:all_types) -> element_position:
    """ Алгоритм бинарного поиска в последовательности

    аргументы:
    seq -- последовательность, в которой будет вестись поиск
    element -- элемент, который нужно найти

    возвращает element_position -- номер позиции элемента (начиная с нуля)
    """
    first = 0
    last = len(seq)-1
    index = -1
    while first <= last and index == -1:
        mid = (first+last)//2
        if seq[mid] == element:
            index = mid
        else:
            if element < seq[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


@benchmark
def exponentiol_search(seq:iterable, element:all_types) -> element_position:
    """ Алгоритм экспоненциального поиска в последовательности

    аргументы:
    seq -- последовательность, в которой будет вестись поиск
    element -- элемент, который нужно найти

    возвращает element_position -- номер позиции элемента (начиная с нуля)
    """
    pass


@benchmark
def interpolation_search(seq:iterable, element:all_types) -> element_position:
    """ Алгоритм интерполяционного поиска в последовательности

    аргументы:
    seq -- последовательность, в которой будет вестись поиск
    element -- элемент, который нужно найти

    возвращает element_position -- номер позиции элемента (начиная с нуля)
    """
    pass


if __name__ == '__main__':
    sequence = [i for i in range(100000)]
    element = randint(0, 99999)
    test_1 = lineal_search(sequence, element)
    test_2 = binary_search(sequence, element)
    test_3 = exponentiol_search(sequence, element)
    test_4 = interpolation_search(sequence, element)

